#include<iostream>
#include<string>

using namespace std;
int main(){
    int t;
    cin >> t;
    for(int p = 0; p<t;p++){

        int flag = 0;
        string s;

        cin>>s;
        int k;

        cin>>k;
        int c = 0;

        for(int i = 0;i<s.size();i++){
            if(s[i]=='-'){
                if(i<=s.size()-k){
                    c++;
                    for(int j=i;j<k+i;j++){
                        if(s[j]=='-')
                            s[j]='+';
                        else
                            s[j]='-';
                    }
                }
                else{
                    flag=1;
                    break;
                }
            }
        }
        cout<<"Case #"<<p+1<<": ";
        if(flag == 1){
            cout<<"IMPOSSIBLE\n";
        }
        else{
            cout<<c<<endl;
        }
    }
}
