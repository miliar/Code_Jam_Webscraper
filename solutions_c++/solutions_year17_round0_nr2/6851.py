#include<bits/stdc++.h>
using namespace std;
#define ll long long


string find_tidy_num(string s){

     if(s.size()==1)
        return s;
    //cout<<s<<endl;
     for(int i=s.size()-1;i>=0;--i){

        if(i==0){

            if(s[i]<=s[i+1]){
                return s;
            }
            if(s[i]=='1')
            {
                //cout<<"s[0] is 1 \n";
                string ans;
                for(int j=0;j<s.size()-1;++j)
                    ans.push_back('9');
                //cout<<ans<<endl;
                return ans;
            }
            //cout<<"here\n";
            for(int j=i+1;j<s.size();++j)
                s[j]='9';
            s[i]=s[i]-1;

            return s;

        }
        else{

            int j=i-1;
            if(j==0 && s[j]>s[i] && s[j]=='1')
                continue;
            if(s[j]>s[i]){

                s[j]=s[j]-1;
                for(int k=i;k<s.size();++k)
                    s[k]='9';

            }
        }

     }


}


int main()
{
    freopen("in22.txt","r",stdin);
    freopen("out22.txt","w",stdout);

    int t;
    scanf("%d",&t);
    int t1=1;
    while(t--){

        printf("Case #%d: ",t1++);
        string s;
        cin>>s;
        string ans= find_tidy_num(s);
        cout<<ans<<endl;
    }

    return 0;
}

