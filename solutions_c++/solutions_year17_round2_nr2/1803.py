#include<bits/stdc++.h>
using namespace std;

int n, q[2000];
/*
void print()
{
    for(int i=1;i<=n;i++)
    {
        int x=q[i];
        if(x==1)printf('R');
        else if(x==2)printf('O');
        else if(x==3)printf('Y');
        else if(x==4)printf('G');
        else if(x==5)printf('B');
        else if(x==6)printf('V');
    }
    printf("\n");
}
*/
int main()
{
    int test=0,testcase,i,j,k,m;
    int h[10];
    //double hh[1111];
    cin>>testcase;

    while(test++ < testcase)
    {
        for(i=0;i<7;i++)cin>>h[i];
        //cin>>h[1]>>h[3]>>h[5];
        printf("Case #%d: ",test);

        string s="";

        if((h[1] + h[3] >= h[5]) && (h[3] + h[5] >= h[1]) && (h[5] + h[1] >= h[3]) )
        {
            if(h[5]>=h[1]&&h[5]>=h[3])
            {
                s.insert(s.begin(),h[5],'B');

                for(i=0;i<h[1];i++)s.insert(s.begin()+i*2,1,'R');

                for(i=0;i<s.size()/2;i++)swap(s[i],s[s.size()-i-1]);

                for(i=0;i<h[3];i++)s.insert(s.begin()+i*2+1,1,'Y');
            }
            else if(h[3]>=h[1]&&h[3]>=h[5])
            {
                s.insert(s.begin(),h[3],'Y');

                for(i=0;i<h[1];i++)s.insert(s.begin()+i*2,1,'R');

                for(i=0;i<s.size()/2;i++)swap(s[i],s[s.size()-i-1]);

                for(i=0;i<h[5];i++)s.insert(s.begin()+i*2+1,1,'B');
            }
            else
            {
                s.insert(s.begin(),h[1],'R');

                for(i=0;i<h[5];i++)s.insert(s.begin()+i*2,1,'B');

                for(i=0;i<s.size()/2;i++)swap(s[i],s[s.size()-i-1]);

                for(i=0;i<h[3];i++)s.insert(s.begin()+i*2+1,1,'Y');
            }
            cout<<s<<endl;
        }
        else{ printf("IMPOSSIBLE\n"); continue; }
        //printf("\n");
        //cout<<result<<endl;
    }

    return 0;
}

