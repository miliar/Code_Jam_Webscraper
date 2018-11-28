#include<bits/stdc++.h>
using namespace std;
int t, l, j;
char s[30];
int main()
{
    FILE *fp, *fc;
    ifstream fin("B-large (1).in");
    ofstream fout("out.txt");
    fin>>t;
    for(int cas=1;cas<=t;cas++){
        fin>>s;
        l = strlen(s);
        for(int i=l-2;i>=0;i--){
            if(s[i] > s[i+1]){
                j = i+1;
                while(j < l)
                    s[j++] = '9';
                s[i]--;
            }
        }
        fout<<"Case #"<<cas<<": ";
        if(s[0] == '0'){
            for(int i=1;i<l;i++)
                fout<<s[i];
        }
        else{
            for(int i=0;i<l;i++)
                fout<<s[i];
        }
        fout<<endl;
    }
    fin.close();
    fout.close();
    return 0;
}

