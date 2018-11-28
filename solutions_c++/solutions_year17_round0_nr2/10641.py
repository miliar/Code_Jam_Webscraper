#include <bits/stdc++.h>
using namespace std;

long long tolonglong(string s)
{
   long long r = 0;
    for(int i=0;s[i];i++)
        r = r * 10 + s[i] - '0';
    return r;
}
string tidy(string ch)
{

int taille=ch.length();
  char c=ch[0];
  for(int i=0;ch[i+1];i++){
                if (ch[i]>ch[i+1]){
                    ch[i]--;
                   int j=i-1;
                   while(ch[j]>ch[i]&&j>=0){
                    ch[j]--;
                    j--;
                   }
                    for(j=i+1;ch[j];j++)
                        ch[j]='9';
                        break;
                }
        }
        if(ch[0]=='0'){
            for(int i=0;i<taille-1;i++){
                ch[i]='9';
            }
            ch[taille-1]='\0';
            return ch;
        }
        if(ch[0]<c){
            for(int i=1;i<taille;i++){
                ch[i]='9';
            }
        }
        return ch;
}
int main()
{
  freopen("B-small-attempt4.in","r",stdin);
   freopen("small_output.txt","w",stdout);


    int T;
     long long k;
    cin>>T;
    int cpt=1;
    while(T--){
    string N;

    cin>>N;
    N=tidy(N);
    k=tolonglong(N);
    cout <<"Case #"<<cpt<<": " << k << endl;
    cpt++;
    }
    return 0;
}
