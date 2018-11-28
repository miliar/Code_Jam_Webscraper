#include <bits/stdc++.h>

using namespace std;

int main()
{
    ifstream fin ("A-large.in");
    ofstream fout ("outputl.txt");
    if(!fin.is_open()) cout<<"the input file didn't open "<<endl;
    if(!fout.is_open()) cout<<"the output file didn't open " <<endl;
    int t,k;
    fin>>t;
    for(int j=1;j<=t;j++){
    string s;
    fin>>s;
    fin>>k;
    int res=0;
    for(int i=0;i<=s.size()-k;i++){
        if(s[i]=='-'){
           int l=i,t=k;
           while(t--){
               if(l==i)res++;
              if(s[l]=='-') s[l++]='+';
              else s[l++]='-';
            }
        }
    }
    bool f=false;
    for(int l=s.size()-1;l>=0;l--){
        if(s[l]=='-'){f=true;break;}
    }
    if(f)fout<<"Case #"<<j<<": "<<"IMPOSSIBLE"<<endl;
    else fout<<"Case #"<<j<<": "<<res<<endl;
    }
     fin.close();
  fout.close();
    return 0;
}
