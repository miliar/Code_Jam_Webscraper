#include <iostream>
#include <fstream>

using namespace std;

int r,c,counter=0;
string cake[30];

bool isletter(char c){
    return ((c<='Z')&&(c>='A'));
}

bool neighbor (int i,int j){
    if (((i>0)&&(isletter(cake[i-1][j])))||((i<r-1)&&(isletter(cake[i+1][j])))
        ||((j>0)&&(isletter(cake[i][j-1])))||((j<c-1)&&(isletter(cake[i][j+1]))))
        return true;
    return false;
}

bool put(int i,int j){
    bool put=true;
    int mini, maxi, k=0;
    if ((i>0)&&(isletter(cake[i-1][j]))) {
        k=0;
        while ((k<j) && (cake[i-1][k]!=cake[i-1][j]))
               k++;
        mini=k;
        k=j;
        while ((k<c)&& (cake[i-1][k]==cake[i-1][j]))
            k++;
        maxi=k-1;
        put=true;
        for (int k=mini;k<=maxi;k++){
            if (cake[i][k]!='?') {
                put=false;
                break;
            }
        }
        if (put) {
            for (int k=mini;k<=maxi;k++) {
                cake[i][k]=cake[i-1][j];counter--;
            }
            return true;
        }
    }

    if ((i<r-1)&&(isletter(cake[i+1][j]))) {
        k=0;
        while ((k<j) && (cake[i+1][k]!=cake[i+1][j]))
               k++;
        mini=k;
        k=j;
        while ((k<c)&& (cake[i+1][k]==cake[i+1][j]))
            k++;
        maxi=k-1;
        put=true;
        for (int k=mini;k<=maxi;k++){
            if (cake[i][k]!='?') {
                put=false;
                break;
            }
        }
        if (put) {
            for (int k=mini;k<=maxi;k++) {
                cake[i][k]=cake[i+1][j]; counter--;
            }
            return true;
        }
    }

    if ((j>0)&&(isletter(cake[i][j-1]))) {
        k=0;
        while ((k<i) && (cake[k][j-1]!=cake[i][j-1]))
               k++;
        mini=k;
        k=i;
        while ((k<r)&& (cake[k][j-1]==cake[i][j-1]))
            k++;
        maxi=k-1;
        put=true;
        for (int k=mini;k<=maxi;k++){
            if (cake[k][j]!='?') {
                put=false;
                break;
            }
        }
        if (put) {
            for (int k=mini;k<=maxi;k++) {
                cake[k][j]=cake[i][j-1];counter--;
            }
            return true;
        }
    }

    if ((j<c-1)&&(isletter(cake[i][j+1]))) {
        k=0;
        while ((k<i) && (cake[k][j+1]!=cake[i][j+1]))
               k++;
        mini=k;
        k=i;
        while ((k<r)&& (cake[k][j+1]==cake[i][j+1]))
            k++;
        maxi=k-1;
        put=true;
        for (int k=mini;k<=maxi;k++){
            if (cake[k][j]!='?') {
                put=false;
                break;
            }
        }
        if (put) {
            for (int k=mini;k<=maxi;k++) {
                cake[k][j]=cake[i][j+1];counter--;
            }
            return true;
        }
    }
}

int main()
{
    ifstream fin("cake.in");
    ofstream fout("cake.out");
    int t;
    fin>>t;
    for (int t1=0;t1<t;t1++){
        fin>>r>>c;
        for (int i=0;i<r;i++)  {
            fin>>cake[i];
        }
//        for (int i=0;i<r;i++){
//            for (int j=0;j<c-1;j++) {
//                if ((cake[i][j]<='Z')&&(cake[i][j]>='A')&&(cake[i][j+1]=='?') )
//                    cake[i][j+1]=cake[i][j];
//            }
//        }
        for (int i=0;i<r;i++)
            for (int j=0;j<c;j++)
                if (cake[i][j]=='?')
                    counter++;

        while (counter>0) {
            for (int i=0;i<r;i++){
                for (int j=0;j<c;j++) {
                    if ((cake[i][j]=='?')&&neighbor(i,j)){
                        put(i,j);
                            //counter--;
                    }
                }
            }
        }
        fout<<"Case #"<<t1+1<<":"<<endl;
        for (int i=0;i<r;i++){
            fout<<cake[i]<<endl;
        }

    }
    return 0;
}
