#include <ncurses.h>
#include <time.h>
#include <stdlib.h>
char waitframe(time_t start,int fps,int next_frame){
    while(1){
        time_t now=time(NULL);
        if((double)(next_frame/fps)<=(now-start))
            return 1;
    }
}
int play(char *fname,int set_fps){
    FILE *f=fopen(fname,"r");
    if(f==NULL){
        puts("Unable to open file!");
        return 2;
    }
    else{
        initscr();
        char chunk[162];
        int framecount=0;
        time_t time_start=time(NULL);
        while(fgets(chunk,sizeof(chunk),f)!=NULL){
            if(chunk[0]=='R'){
                move(0,0);
                waitframe(time_start,set_fps,framecount);
                framecount++;
            }
            else{
                addstr(chunk);
                refresh();
            }
        }
        endwin();  
        return 0;
    }         
}
int main(int argc, char *argv[]){
    if(argc !=3)
        printf("Usage: %s <file_name> <fps>\n",argv[0]);
    else
        return play(argv[1],atoi(argv[2]));
}
