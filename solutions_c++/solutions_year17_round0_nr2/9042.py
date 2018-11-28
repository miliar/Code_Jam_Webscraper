#include <iostream>
#include <sstream>
using namespace std;
int check(long long a){
    ostringstream ss;
    ss<<a;
    string Result;
    Result = ss.str();
    int l=Result.length();
    int flag=1;
    for(int i =l-1;i>0;i--){
        if(Result[i]<Result[i-1])
            flag=0;
    }
    return flag;
}
int main()
{
    int K;
    cin>>K;
    for(int a=1;a<=K;a++){
        long long x;
        cin>>x;
        int flag=0;
        while(flag==0){
            if(check(x)==1){
                cout<<"Case #"<<a<<": "<<x<<endl;
                break;
            }
            x--;
        }
    }
    return 0;
}
