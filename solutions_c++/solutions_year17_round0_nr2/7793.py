#include <iostream>
#include <string>
#include <vector>
#include <fstream>
using namespace std;
unsigned int t;
int indx;
string n;
vector<string> v;
int check();
int main()
{
    cin>>t;v.resize(t);
    for(unsigned int i=0;i<t;++i){
        cin>>n;
        while((indx=check())!=-1){
            n[indx]-=1;
            for(int j=indx+1;j<n.length();++j)n[j]='9';
            if(n.find_first_not_of('0')!=0)
                n.erase(0,n.find_first_not_of('0'));
        }
        v[i]=n;
    }
    ofstream output;
    output.open("/home/mina/CLionProjects/cf/output");
    for (unsigned int i = 0; i <t ; ++i) output<<"Case #"<<i+1<<": "<<v[i]<<endl;
    return 0;
}
int check(){
    for(unsigned int i=0;i<n.length()-1;++i){
        if(n[i]>n[i+1])return i;
    }
    return -1;
}
