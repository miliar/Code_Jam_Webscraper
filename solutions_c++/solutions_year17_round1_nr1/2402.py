#include<bits/stdc++.h>
using namespace std;
char s[30][30], x[30][30];
int r, c;
void ass(int I, int J)
{
    int f, col=J, se, i, j, flag=0, J1=J;
    i = I-1;
    while(i>=0 && x[i][J]=='?'){
        i--;
    }
    f = i+1;
    i = I+1;
    while(i<r && x[i][J] == '?')
        i++;
    se = i-1;
    j = J+1;
    while(j < c){
        for(i=f;i<=se;i++){
        if(x[i][j] != '?'){
            flag = 1;
            break;
        }}
        if(flag)
            break;
        col = j;
        j++;
    }
    j = J-1;
    flag = 0;
    while(j >= 0){
        for(i=f;i<=se;i++){
        if(x[i][j] != '?'){
            flag = 1;
            break;
        }}
        if(flag)
            break;
        J1 = j;
        j--;
    }

    for(int i=f;i<=se;i++)
        for(int j=J1;j<=col;j++)
            x[i][j] = s[I][J];
}
int main()
{
    //FILE *fp, *fc;
    int t;
    ifstream fin("A-large.in");
    ofstream fout("out.txt");
    fin>>t;
    for(int cas=1;cas<=t;cas++){
        fin>>r>>c;
        for(int i=0;i<r;i++){
            fin>>s[i];

        }
        for(int i=0;i<r;i++){
            for(int j=0;j<c;j++){
                x[i][j] = s[i][j];
            }
        }
        for(int j=0;j<c;j++){
            for(int i=0;i<r;i++){
                if(s[i][j] != '?')
                    ass(i, j);
            }
        }
        fout<<"Case #"<<cas<<":"<<endl;
        for(int i=0;i<r;i++){
            for(int j=0;j<c;j++){
                fout<<x[i][j];
            }
            fout<<endl;
        }
    }
    fin.close();
    fout.close();
    return 0;
}
