#include <iostream>
using namespace std;
int main()
{
    int t,k,p=0;
    cin >> t;
    for(k=0;k<t;k++){
        int i,n,c=0,flag=0;
        string str;
        cin >> str;
        cin >> n;
        int len = str.length();
        for(i=0;i<len;i++)
        {
            if(str[i]=='-'){
                if(i<=len-n){
                c++;
                for(int j=i;j<i+n;j++){
                    if(str[j]=='-')
                        str[j]='+';
                    else
                        str[j]='-';
                }
            }

            else{
                flag=1;
                break;
            }
        }
        }
    cout<<"Case #"<<p+1<<": ";
    if(flag==1)
        cout<<"IMPOSSIBLE";
    if(flag==0)
        cout<<c;
    p++;
    cout<<endl;
}
    return 0;
}
