#include <bits/stdc++.h>
#define Write freopen("out.txt","w",stdout)
#define Read freopen("in.txt","r",stdin)
#define sf(a) scanf("%d",&a)
#define sff(a,b) scanf("%d %d",&a,&b)
#define sfff(a,b,c) scanf("%d %d %d",&a,&b,&c)
#define ll long long
#define mod 100000007
#define MAXX 100
using namespace std;
//int arr[10];
//int lft[10];
//int rgt[10];
//int main()
//{
//    int tc;
//    cin>>tc;
//    for(int tt=1; tt<=tc; tt++)
//    {
//        int x;
//        sf(x);
//        for(int i=1; i<=x; i++)
//        {
//
//            sf(arr[i]);
//        }
//        stack<int>st;
//        for(int i=1; i<=x; i++)
//        {
//            int p;
//            p=arr[i];
//            if(st.empty())
//            {
//                st.push(i);
//            }
//            else
//            {
//                while(!st.empty()&&arr[st.top()]>=p)
//                {
//                    cout<<st.top()<<endl;
//                    st.pop();
//                ////cout<<st.top()<<endl;
//                }
//
//                if(st.empty())
//                {
//                    arr[i]=0;
//                    st.push(i);
//                    cout<<"p"<<i<<endl;
//                }
//
//                else
//                {
//                    lft[i]=st.top();
//                    st.push(i);
//                cout<<st.top();
//                    cout<<"p"<<i<<endl;
//                }
//
//            }
//        }
//        for(int i=1;i<=7;i++){
//            cout<<lft[i]<<" ";
//        }
//        cout<<endl;
//    }
//}
bool check(int x)
{

    int b=x%10;
    x=x/10;
    while(x!=0)
    {
        int c=x%10;
        if(b<c) return false;
        b=c;
        x=x/10;
    }
    return true;





}
int main()
{   Read;
    Write;
    int a;
    cin>>a;
    for(int tt=1;tt<=a;tt++)
    {
        int k;
        cin>>k;
        for(int i=k;i>=0;i--){
            if(check(i)){
                cout<<"Case #"<<tt<<": "<< i<<endl;
                break;
            }
        }
    }
}
