#include <iostream>
#include <fstream>
#include <string.h>
#include <string>
#include <stdlib.h>

using namespace std;

bool all_up(int len, char pancake[]){
    for(int i=0; pancake[i]!='\0'; ++i){
        if(pancake[i]=='-') return false;
    }
    return true;
}

int minimun(const int len1,char pancake2[], int start, int finish,int limit){
    int j;
    int len = len1;
    //int k;
    //int l = len - 2;
    int s1;
    int s2;
    int sol = 0;
    char pancake[1000];
    char pancake1[1000];

    memcpy(pancake1,pancake2,1000);

    for (int i = start; i<finish+1; i=i+1)
    {
        if(pancake1[i]=='-')pancake1[i] = '+';
        else pancake1[i]='-';
    }
    memcpy(pancake,pancake1,1000);

    if(all_up(len,pancake))
        return 0;
    else if(len <limit ){
        return 30000;
    }
    else{
        memcpy(pancake,pancake1,1000);
        s1 = minimun(len - 1, pancake, 0, -1, limit);
        memcpy(pancake,pancake1,1000);
        s2 = minimun(len - 1, pancake, len - limit, len - 1, limit) + 1;
        sol = min( s1  , s2 );
    }
    return sol;
}

int main()
{
    char a[100];
    char pancake[1000];
    int no_of_elem = 0;
    int buf;
    int limit;
    ofstream outfile;
    outfile.open("out.txt");
    ifstream infile;
    infile.open("A-small-attempt1.in");

    infile >> a;
    no_of_elem = atoi(a);

    for (int i = 0; i < no_of_elem; ++i){
        memset(pancake,'\0',1000);
        infile >> pancake;
        infile >> a;
        limit = atoi(a);
        buf = minimun(strlen(pancake),pancake,0,-1,limit);
        if(buf >= 30000){
            outfile << "Case #" << i+1 << ": IMPOSSIBLE" << endl;
        }
        else outfile << "Case #" << i+1 << ": " << buf << endl;
    }

    outfile.close();
    infile.close();

    return 0;
}
