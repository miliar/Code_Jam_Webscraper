#include <bits/stdc++.h>
using namespace std;

int findI(int len,string s){

    for(int i=0;i<len;i++){
        if(s[i]=='-'){
            return i;
        }
    }
    return -1;
}

int main(){


    freopen("A-large.in","r",stdin);
    freopen("o1large.txt","w",stdout);


    int t;
    scanf("%d",&t);

    for(int g=1;g<=t;g++){

        string s;
        int k;
        cin>>s>>k;
        int len = s.length();
        int ans=0;
        int flg=0;
        while(1){

        //cout<<"===============================";
            //cout<<s<<endl;
            int index = findI(len,s);
            //cout<<"Index:"<<index<<endl;
            //int u;
            //cin>>u;

            if(index<0){
                break;
            }
            if((index+k-1)>=len){
                flg=1;
                break;
            }
            else{
                for(int i=index;i<index+k;i++){
                    if(s[i]=='-'){
                        s[i]='+';
                    }else if(s[i]=='+'){
                        s[i]='-';
                    }

                }
                ans++;
            }

        }
        cout<<"Case #"<<g<<": ";
        if(!flg)
            cout<<ans<<endl;
        else{
            cout<<"IMPOSSIBLE\n";
        }
    }
    return 0;
}
