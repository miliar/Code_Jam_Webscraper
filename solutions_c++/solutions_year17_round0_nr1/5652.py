#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <map>
#include <string>

const int length_size = 1200;
std::map<std::string, int> lists[length_size];
char data[length_size] = {0};
int iteration = 0;
int cur_length = 0;
// To iterate, we need to flip all combinations, and save them.
void iterate(int k)
{
    char in[5];
    //printf("In! %s %d %d\n", data, strlen(data), strlen("---+-++-"));

    int i;
    int j;

    lists[k][data] = iteration;
    for(i = 0; i <= cur_length - k; i++){
        // First, flip a combo
        //printf("B: %s\n", data);
        for(j = 0; j < k; j++){
            if(data[i+j] == '+')
                data[i+j] = '-';
            else if(data[i+j] == '-')
                data[i+j] = '+';
        }

       // printf("A: %s\n", data);
        iteration++;
       // printf("%d\n", lists[k].count(data));
        //Check if there is value in continuing down this path.
        if(lists[k].count(data) == 0 || iteration < lists[k][data]){
            iterate(k);
        }
        iteration--;
        // Unflip.
        for(j = 0; j < k; j++){
            if(data[i+j] == '+')
                data[i+j] = '-';
            else if(data[i+j] == '-')
                data[i+j] = '+';
        }
    }
   // printf("Out! %d\n", iteration);
}

int main()
{
    FILE *in = fopen("in.txt", "r");
    FILE *out = fopen("out.txt", "w");
    char buf[1200];
    fgets(buf, 400, in);
    int cases = 1;
    while(fgets(buf, 1200, in))
    {
        while(buf[strlen(buf)-1] == '\n' || buf[strlen(buf)-1] == '\r')
            buf[strlen(buf)-1] = '\0';

        int i;
        int k;
        sscanf(buf, "%s %d", &data, &k);
        char orig[1200];
        strcpy(orig, data);
        for(i = 0; i < strlen(orig); i++){
            data[i] = '+';
        }
        cur_length = i;
        data[i] = '\0';
        iterate(k);
        printf("%s %d\n", orig, lists[k].count(orig));
        //fgets(buf, 10, stdin);
        if(lists[k].count(orig) == 0){
            fprintf(out, "Case #%d: IMPOSSIBLE \n", cases++, lists[k][orig]);
        }
        else{
            fprintf(out, "Case #%d: %d\n", cases++, lists[k][orig]);

        }
    }
    return 0;
}
