#include <stdio.h>
#include <stdlib.h>
int validLine(char buff[], int len);
int getNum(char c){
    return atoi(&c);
}
int validLine(char buff[], int len){
    for(int i = 0; i < len-2; i++){
        if(getNum(buff[i]) > getNum(buff[i+1]))
            return 0;
    }
    return 1;
}

int main(int argc, char *argv[]){
    FILE * f;
    f = fopen("input.txt", "r");
    char * line = NULL;
    size_t len = 0;
    ssize_t read;
    int rest = 0;
    int ff;
    int spot;
    int lessone;
    int ccase = 1;
    FILE * out;
    out = fopen("output", "w");
    read = getline(&line, &len, f);
    int z = atoi(line);
    for(int i = 0; i < z; i++){
        read = getline(&line, &len, f);
        len = read;
        fprintf(out,"Case #%d: ", ccase );
        if(validLine(line, len)){
            fprintf(out,"%s", line);
            ccase++;
            continue;
        }
        spot = 0;
        lessone = 0;
        for(int t = len -2; t > 0; t--){

            if(getNum(line[t]) < getNum(line[t-1])){

                ff = getNum(line[t-1]);
                ff--;
                if(ff == 0 && t == 1){
                    lessone = 1;
                }
                if(f == 0){
                    f = 0;
                }

                line[t-1] = 48 + ff;
                spot = t-1;

            }


        }
        if(lessone){
            for(int u = 0; u < len -2; u++){
                fprintf(out,"9");
            }
        }else{
            for(int u = 0; u <= spot; u++){
                fprintf(out, "%c", line[u]);
             }
            for(int u = spot+1; u <  len -1; u++){
                fprintf(out, "9");
            }
        }
        ccase++;
        fprintf(out,"\n");

    }
    exit(0);

}

