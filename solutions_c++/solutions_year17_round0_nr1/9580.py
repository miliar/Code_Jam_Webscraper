#include <bits/stdc++.h>
using namespace std;

int main()
{
    long long t,i;
    cin>>t;
    long long r=1;
    while(r!=(t+1)){
        string s;
        long long k;
        cin>>s>>k;
        int cnt=0,pos;
        int flag=0,flag1;
        pos=-1;
        while(true){
                flag1=0;
        for(i=0;i<s.length();i++){
            if(s[i]=='-'){
                    pos=i;
                    //cout<<"pos:"<<pos;
                    break;
            }

        }
        if(pos == -1){
            cnt=0;
           // cout<<"cnt: "<<cnt;
            break;
        }
       else if((pos+k)>s.length()){
            flag=2;
            //cout<<"flag: "<<flag;
            break;
        }

        else{
        cnt++;
        for(int i=pos;i<(pos+k);i++){

           if(s[i]=='+'){
                s[i]='-';
            }
            else
                s[i]='+';
        }
        for(i=0;i<s.length();i++)
        {
            if(s[i]=='-')
            {
                flag1=1;
            }
        }
        long long cnt_m=0, cnt_p=0;
       /* for(int i=pos;i<(pos+k);i++){

            if(s[i]=='+'){
                cnt_p++;
            }
            else
                cnt_m++;
        }
        if(cnt_m==cnt_p){
            flag=2;
            break;
        }*/
        }
          if(flag1==0)
    {
        break;
    }

    }
        //cout<<cnt<<"\n";
       // cout<<pos<<"\n";

    if(flag==2){
       cout<<"Case #"<<r<<": "<<"IMPOSSIBLE"<<"\n";
    }
     if(flag1==0 && pos!=-1 && flag!=2 ){
     cout<<"Case #"<<r<<": "<<cnt<<"\n";
    }
     if(pos==-1)
    {
      cout<<"Case #"<<r<<": "<<cnt<<"\n";
    }
    r++;
    }
    return 0;
}
