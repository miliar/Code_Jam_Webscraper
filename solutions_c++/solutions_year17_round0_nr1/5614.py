#include<bits/stdc++.h>
using namespace std;

int main()
{
    int t;
    ifstream in;
    in.open("A-large.in");
    in >> t;
    ofstream out;
    out.open("result.txt");
    for(int cs=0;cs<t;cs++) {
        string s;
        in >> s;
        int k;
        in >> k;
        int l = s.length();
        int flagImp = 0;
        int flips=0;
        for(int i=0;i<l;i++)
        {
            if(s[i]=='-'){
                if((l-i)<k){
                    flagImp = 1;
                    break;
                }
                else{
                    flips++;
                    for(int j=i;j<i+k;j++){
                        if(s[j]=='-'){
                            s[j]='+';
                        }
                        else{
                                s[j]='-';
                        }
                    }
                }
            }
        }
        if(flagImp==1){
            out << "Case #"<<cs+1<<": IMPOSSIBLE\n";
        }
        else{
            out << "Case #"<<cs+1<<": "<<flips<<"\n";
        }
    }
    return 0;
}
