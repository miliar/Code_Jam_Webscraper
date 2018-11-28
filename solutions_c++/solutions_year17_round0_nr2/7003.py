#include <bits/stdc++.h>
using namespace std;
int main()
{
	freopen("B-large.in","r",stdin);
    freopen("output_file.out","w",stdout);
    int m;
    cin>>m;
    for(int h=0;h<m;h++)
    {
        long long x,y,z=0,exp;
        cin>>x;
        exp=x;
        while(exp>0)
        {
        	exp=exp/10;
        	z++;
        }
        //string s=to_string(x);
        //cout<<s<<endl;
        //z=s.size();
        int a[z];
        int p=z-1;
        while(x>0)
        {
            y=x%10;
            x=x/10;
            a[p]=y;
            p--;
            //cout<<y<<endl;
        }
        int i=z-2,j=z-1,k=0;
        while(i > -1)
        {
            if(a[i]<=a[j])
            {
                i--;
                j--;
            }
            else
            {
                a[i]--;
                for(k=j;k<z;k++)
                {
                    a[k]=9;
                }
            }
        }
        int q;
        for (int i = 0; i < z; i++) {
            if(a[i] != 0)
            {
                q=i;
                break;
            }
        }
        cout<<"Case #"<<h+1<<": ";
        for(int i=q;i<z;i++)
        {
            cout<<a[i];
        }
        cout<<endl;
    }
    fclose (stdin);
    fclose (stdout);
    return 0;
}
