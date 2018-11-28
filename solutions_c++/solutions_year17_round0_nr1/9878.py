#include <iostream>
#include <vector>
using namespace std;
int main()
{
    string s;int i,k,j,t,ans=0;
    cin>>t;
    int mm=1;
    while(mm<=t){
        cin>>s>>k;
        vector <bool> arr(s.size());
        for(i=0;i<s.size();i++){
            if(s[i]=='+')
                arr[i]=true;
            else
                arr[i]=false;
        }
        ans=0;
        for(i=0;i<=s.size()-k;i++){
            if(!arr[i]){
                ans++;
                for(j=i;j<i+k;j++){
                    arr[j]=!arr[j];
                }
            }
        }
        while(i<s.size()){
            if(!arr[i]){
                cout<<"Case #"<<mm<<": IMPOSSIBLE\n";goto EXIT;
            }
            i++;
        }
        cout<<"Case #"<<mm<<": "<<ans<<"\n";
        EXIT:mm++;
    }
    return 0;
}
