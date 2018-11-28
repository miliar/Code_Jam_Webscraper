#include <bits/stdc++.h>
using namespace std;
struct node{
    char str[26];
};
int main() {
    int T;
    cin>>T;
    for(int j=1;j<=T;j++)
    {
        cout<<"Case #"<<j<<":"<<endl;
        int S,C;
        cin>>S>>C;
        int i,k;
        node a[S];
        for(i=0;i<S;i++)
        {
            scanf("%s",a[i].str);
        }
        int H1[26],V1[26],H2[26],V2[26];
        for(i=0;i<26;i++)
        {
            H1[i]=-1;
            H2[i]=-1;
            V1[i]=-1;
            V2[i]=-1;
        }
        for(i=0;i<S;i++)
        {
            for(k=0;k<C;k++)
            {
                if(a[i].str[k]!='?')
                {
                    int x= a[i].str[k] - 'A';
                    if(H1[x]==-1)
                    {
                        H1[x]=i;
                        H2[x]=i;
                        V1[x]=k;
                        V2[x]=k;
                    }
                    else
                    {
                        H2[x]=i;
                        V2[x]=k;
                    }
                }
            }
        }
        for(i=0;i<26;i++)
        {
            char x= i+'A';
            if(H1[i]!=-1)
            {
                for(k=H1[i];k<=H2[i];k++)
                {
                    for(int l=V1[i];l<=V2[i];l++)
                    {
                        a[k].str[l]=x;
                    }
                }
            }
        }
        for(i=0;i<S;i++)
        {
            char x= a[i].str[0];
            int cont=0;
            for(k=0;k<C;k++)
            {
                if(a[i].str[k]=='?')
                    a[i].str[k]=x;
                else
                {
                    cont++;
                    x=a[i].str[k];
                }
            }
            x= a[i].str[C-1];
            for(k=C-1;k>=0;k--)
            {
                if(a[i].str[k]=='?')
                    a[i].str[k]=x;
                else
                {
                    cont++;
                    x=a[i].str[k];
                }
            }
            if(cont==0&&i!=0)
            {
                for(k=0;k<C;k++)
                    a[i].str[k]=a[i-1].str[k];
            }
        }
        for(i=S-2;i>=0;i--)
        {
            int cont=0;
            for(k=0;k<C;k++)
            {
                if(a[i].str[k]!='?')
                    cont++;
            }
            if(cont==0)
            {
                for(k=0;k<C;k++)
                    a[i].str[k]=a[i+1].str[k];
            }
        }
        for(i=0;i<S;i++)
        {
            printf("%s",a[i].str);
            cout<<endl;
        }
    }
	// your code goes here

	return 0;
}
