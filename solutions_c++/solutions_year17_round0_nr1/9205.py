#include <iostream>
#include <fstream>
using namespace std;

int main()
{
  ifstream myfile;
  ofstream outfile("output.txt");
  //set<int> vtr;
  myfile.open ("input.txt");
  int tests;
  myfile>>tests;
  for(int v=1;v<=tests;v++){
        string s;
        myfile>>s;
        int n;
        int flag=0;
        int i;
        myfile>>n;
        //cout<<s;
        //cout<<"n";
        //cout<<n;
        for(i=0;i<s.length()-n+1;i++){
            if(s[i]=='-'){
                //cout<<i;
                //cout<<s;
                for(int j=i;j<i+n;j++){
                    if(s[j]=='-')
                        s[j]='+';
                    else
                        s[j]='-';
                }
                flag++;
            }
        }
        //cout<<s;
        for(;i<s.length();i++){
            if(s[i]=='-'){
                flag=-1;
                break;
            }
        }
        
        //string p;
        if(flag==-1)
            outfile<<"Case #"<<v<<": "<<"IMPOSSIBLE"<<endl;
        else
            outfile<<"Case #"<<v<<": "<<flag<<endl;
         
         continue;
       }
       return 0;
        
}
