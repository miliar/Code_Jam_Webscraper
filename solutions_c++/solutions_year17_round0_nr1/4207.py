#include <bits/stdc++.h>
using namespace std;
int main()
{
    ifstream inp("A-large.in");
    ofstream op;
    op.open("GCJ17A.txt",ios_base::app);
    int tc,caseno=1;
    inp>> tc;
    while(tc--){
        int k,cnt=0;
        string s;
        inp>> s >> k;
        for(int a=0;a<=s.length()-k;a++){
            if(s[a]=='-'){
                for(int b=a;b<a+k;b++) s[b]=(s[b]=='+')?'-':'+';
                cnt++;
            }
        }
        bool flag=false;
        for(int a=s.length()-k+1;a<s.length();a++){
            if(s[a]=='-'){
                flag=true;
                break;
            }
        }
        if(flag){
            op<< "Case #" << caseno++ << ": IMPOSSIBLE" <<endl;
            continue;
        }
        op<< "Case #" << caseno++ << ": " << cnt <<endl;
    }
    op.close();
    return 0;
}
