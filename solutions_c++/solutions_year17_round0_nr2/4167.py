#include <bits/stdc++.h>
using namespace std;
bool issorted(long long int n)
{
    char arr[20];
    sprintf(arr,"%lld",n);
    string st=string(arr);
    sort(st.begin(),st.end());
    if(st==string(arr)) return true;
    return false;
}
int main()
{
    ifstream inp("B-large.in");
    ofstream op;
    op.open("GCJ17A.txt",ios_base::app);
    int tc,caseno=1;
    inp>> tc;
    while(tc--){
        long long int n;
        inp>> n;
        if(issorted(n)){
            op<< "Case #" << caseno++ << ": " << n <<endl;
            continue;
        }
        bool flag=false;
        for(int a=0;a<19;a++){
            if((long long int)pow(10,a)==n){
                op<< "Case #" << caseno++ << ": " << n-1 <<endl;
                flag=true;
                break;
            }
        }
        if(flag) continue;
        char arr[20];
        sprintf(arr,"%lld",n);
        string num=string(arr);
        for(int a=num.length()-1,b=a-1;a>0;a--,b--){
            if(num[b]>num[a]){
                for(int b=a;b<num.length();b++) num[b]='9';
                num[b]--;
            }
        }
        sscanf(num.c_str(),"%lld",&n);
        op<< "Case #" << caseno++ << ": " << n <<endl;
    }
    op.close();
    return 0;
}
