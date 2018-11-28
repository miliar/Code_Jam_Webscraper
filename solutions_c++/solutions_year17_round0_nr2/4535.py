#include<bits/stdc++.h>
using namespace std;

int main()
{
    fstream input("tidynumbers.txt",std::ios_base::in);
    ofstream output;
    output.open("output2.txt");
    int arr[20],r_arr[20],ans[20];
    int T;input>>T;
    for(int t=1;t<=T;t++)
    {
        long long n;input>>n;
        int i=0,j=0;
        while(n)
            r_arr[i++]=n%10,n=n/10;
//        cout<<"r_arr is "<<endl;
//        for(int m=0;m<i;m++)
//            cout<<r_arr[m];
//        cout<<endl;
        while(--i>=0)
            arr[j++]=r_arr[i];
//        cout<<"Arr is "<<endl;
//        for(int m=0;m<j;m++)
//            cout<<arr[m];
//        cout<<endl;
        i=1;
        while(i<j&&arr[i]>=arr[i-1])
        {
//            cout<<"i is "<<i<<" and arr[i-1] is "<<arr[i-1]<<endl;
            ans[i-1]=arr[i-1];
            i++;
        }
//        cout<<"break point is "<<i-1<<endl;
//        cout<<"ans is "<<endl;
//        for(int m=0;m<i-1;m++)
//            cout<<ans[m];
//        cout<<endl;
//        cout<<"arr is "<<endl;
//        for(int m=0;m<i;m++)
//            cout<<arr[m];
//        cout<<endl;
        if(arr[i-1]==1)
        {
            ans[i-1]=arr[i-1];
            if(i<j)
            {
                ans[0]=0;
                for(int k=1;k<j;k++)
                    ans[k]=9;
            }
            long long a=0;
            for(int k=0;k<j;k++)
                a=a*10+ans[k];
            output<<"Case #"<<t<<": "<<a<<"\n";
        }
        else
        {
            ans[i-1]=arr[i-1];
            int m=i-1;
            if(i<j)
            {
                int x=arr[i-1];
                //output<<"x is "<<x<<"\n";
                m=i-1;
                while(m>=0&&arr[m]==x)
                    m--;
                //output<<"m is "<<m<<"\n";
                m++;
                ans[m]--;
                //output<<"ans[m] is "<<ans[m]<<"\n";
            }
            //output<<"m is "<<m<<"\n";
            for(int k=m+1;k<j;k++)
                ans[k]=9;
            long long a=0;
            for(int i=0;i<j;i++)
                a=a*10+ans[i];
            output<<"Case #"<<t<<": "<<a<<"\n";
        }
    }
}
