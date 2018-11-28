#include<bits/stdc++.h>
using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("APancakeFlipperlarge2.out","w",stdout);
    int T, cs=0;
    scanf("%d", &T);
    getchar();
    while(T--)
    {
        string str;
        cin>>str;
        int k;
        scanf("%d", &k);

        int len = str.size();
        int s = 0;
        int count=0;
        while(1)
        {
            if( (s + k) > len){
                break;
            }

            if(str[s]!='+')
            {
               count++;
               //cout<<"\ns: "<<s<<"\n";
               for(int i=0; i<k; i++){
                   if(str[s+i]=='-')
                    str[s+i]='+';
                   else
                    str[s+i]='-';
                    //cout<<"i"<<s+i<<" "<<str<<"\n";
               }
            }
            s++;
        }

        int flag=0;
        for(int i=0; i<len; i++){
            if(str[i]=='-'){
                flag=1;
                break;
            }
        }
        //cout<<"\nChang: "<<str<<"\n";
        if(flag==1) printf("Case #%d: IMPOSSIBLE\n", ++cs);
        else printf("Case #%d: %d\n", ++cs, count);
    }


    return 0;
}

