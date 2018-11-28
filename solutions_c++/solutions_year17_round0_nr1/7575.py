#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
int main()
{
    int q;
    cin>>q;
    vector <int> a;
    while(q--)
    {
        int t;
        cin>>t;
        switch(t)
        {
        case 1:
            {
                long long int n;
                cin>>n;
                a.push_back(n);
            }
        break;
        case 2:
            {
                long long int p;
                cin>>p;
                a.erase(a.begin()+(p-1));
            }
        break;
        case 3:
            {
                long long int n,p;
                cin>>p>>n;
                a[p-1]=n;
            }
        break;
        case 4:
            {
                long long int l,r,k,n,i,j;
                cin>>l>>r>>k;
                int c[r-l+1];
               // c.insert(c.begin(),a.begin()+l-1,a.begin()+r-1);
                for(i=l-1,j=0;i<r;i++,j++)
                {
                    
                    c[j]=a[i];                    
                   // cout<<c[j]<<" ";
                    
                }
                sort(c,c+j);
                cout<<c[k-1]<<endl;
            }
        break;

        }
    }
    return 0;
}
