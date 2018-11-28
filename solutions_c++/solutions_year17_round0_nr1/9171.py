#include<bits/stdc++.h>

using namespace std;
int check(string s)
    {
    int flag=0;
    for(int i=0;i<s.size();i++)
        if(s[i]=='-')
        {
        flag=1;
        break;
    }
    if(flag==0)
        return 0;
    else return 1;
}

int main(){
    int qq,i,cnt=0,k,p;
    string s;
    cin>>qq;
    while(qq--)
        { int n=0;int flag=1;
        cnt++;
        printf("Case #%d: ",cnt);
        cin>>s;
        scanf("%d",&k);
        for(int i=0;i<s.size();i++)
            {p=check(s);
             int j=0;
            if(s.size()>=k+i&&p==1)
        {if(s[i]=='-')
            {
            n++;
            j=0;
            while(j<k)
                {
                if(s[j+ i]=='+')
                    s[j+i]='-';
                else
                    s[j+i]='+';
                j++;
            }
        }
        }
         
         else if(!(s.size()>=k+i))
         {    flag=0;
          break;
          
         }
            }
         if(p==1)
             cout<<"IMPOSSIBLE"<<endl;
         else
             cout<<n<<endl;
    }
    return 0;
}

