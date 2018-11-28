#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("in4.txt","r",stdin);
    freopen("out4.txt","w",stdout);
    int T;
    cin>>T;
    for(int tc=1;tc<=T;tc++){
        int n, arr[6]={0},o,v,g;
        cin>>n;
        for(int f=0;f<6;f++){
            cin>>arr[f];
        }
        string ans,S="ROYGBV";
        if(arr[1]>arr[4]||arr[3]>arr[0]||arr[5]>arr[2])
        {
            ans="IMPOSSIBLE";
        }
        else
        {
            o=arr[1];
            v=arr[5];
            g=arr[3];
            arr[4]-=o;
            arr[1]-=o;
            arr[0]-=g;
            arr[3]-=g;
            arr[2]-=v;
            arr[5]-=v;
            n-=2*o+2*g+2*v;
            for(int f=0;f<6;f++)
                for(int f1=f+1;f1<6;f1++)
                {
                    if(arr[f]<arr[f1])
                    {
                        swap(arr[f],arr[f1]);
                        swap(S[f],S[f1]);
                    }
                }
            for(int f=0;f<n;f++)
                ans+=".";
            int c=0;
            for(int f=0;f<n;f+=2)
            {
                while(!arr[c])
                    c++;
                ans[f]=S[c];
                arr[c]--;
            }
            for(int f=1;f<n;f+=2)
            {
                while(!arr[c])
                    c++;
                ans[f]=S[c];
                arr[c]--;
            }
            if(ans==""&&o)
                ans="BO",o--;
            if(ans==""&&v)
                ans="YV",v--;
            if(ans==""&&g)
                ans="RG",g--;
            for(int f=0;f<ans.size();f++)
            {
                if(ans[f]=='B'&&o)
                {
                    while(o)
                    {
                        ans.insert(f,"BO");
                        o--;
                    }
                }
                if(ans[f]=='R'&&g)
                {
                    while(g)
                    {
                        ans.insert(f,"RG");
                        g--;
                    }
                }
                if(ans[f]=='Y'&&v)
                {
                    while(v)
                    {
                        ans.insert(f,"YV");
                        v--;
                    }
                }
            }
            for(int f=0;f<ans.size();f++)
            {
                if(ans[f]==ans[(f+1)%ans.size()]||o||g||v){
                    ans="IMPOSSIBLE";
                    break;
                }
            }
        }
        cout<<"Case #"<<tc<<": ";
        cout<<ans<<endl;
    }
}
