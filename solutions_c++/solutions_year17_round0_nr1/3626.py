#include <iostream>
#include<fstream>

using namespace std;

int main()
{
int T;
cin>>T;
ofstream fout("out.txt");
for(int x=0;x<T;x++){
    string s;
    cin>>s;
    int L;
    cin>>L;
    int sum=0;
    for(int y=0;y<s.length()-L+1;y++){
        if(s[y]=='-'){
            sum++;
            s[y]='+';
            for(int z=y+1;z<y+L;z++){
            if(s[z]=='-'){
                s[z]='+';
            }else{
                s[z]='-';
            }
            }

        }
    }
    fout<<"Case #"<<x+1<<": ";
   for(int y=s.length()-1;y>s.length()-L;y--)if(s[y]=='-'){fout<<"IMPOSSIBLE"<<endl;goto out;}
   // if(s[s.length()-1]=='-' || s[s.length()-2]=='-'){cout<<"IMPOSSIBLE"<<endl;continue;}
    fout<<sum<<endl;
    out:;
}
}
