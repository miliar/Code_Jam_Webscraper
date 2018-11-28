#include <iostream>
#include <string>
#include <vector>
#include <fstream>
using namespace std;
unsigned int t,k;
unsigned long l;
string s;
vector<int>v;
int main()
{
    cin>>t;v.resize(t,0);
    for(unsigned int i=0;i<t;++i) {
        cin >> s >> k;
        l = 0;
        while (l < s.length()) {
            l = s.find_first_of('-');
            if(l!=string::npos){
                if(s.length()-l>=k){
                    for(unsigned long j=l;j<l+k;++j){
                        if(s[j]=='-')s[j]='+';
                        else s[j]='-';
                    }
                    ++v[i];
                }
                else {
                    v[i]=-1;
                    break;
                }
            }
        }
    }
    ofstream output;
    output.open("/home/mina/CLionProjects/cf/output");
    for (unsigned int i = 0; i <t ; ++i){
        output<<"Case #"<<i+1<<": ";
        if(v[i]!=-1)output<<v[i];
        else output<<"IMPOSSIBLE";
        output<<endl;
    }
    return 0;
}
