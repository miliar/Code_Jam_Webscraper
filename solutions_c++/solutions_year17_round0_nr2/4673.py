#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t;
    long long int n;
    cin>>t;
    for(int h=1;h<=t;h++)
    {
        cin>>n;
         int m;
        vector<int>vec;
        int count1=0;
        while(n!=0)
        {
            m=n%10;
            n=n/10;
            count1++;
            vec.push_back(m);
        }
        int arr[count1];
        for(int j=vec.size()-1;j>=0;j--)
            arr[count1-j-1]=vec[j];
        //for(int j=0;j<count1;j++)
          //  cout<<arr[j];
        for(int i=0;i<count1-1;i++)
        {
            int j=i+1;
            if(arr[i]<=arr[j])
                continue;
            else
            {
                if(arr[i]!=1)
                {
                    int d=i;
                    while(1)
                    {
                    arr[d]=arr[d]-1;
                    for(int k=d+1;k<count1;k++)
                        arr[k]=9;
                     if(d!=0&&arr[d]<arr[d-1])
                     {
                         d=d-1;
                         continue;

                     }
                     else
                     {
                         //out=1;
                         break;

                     }


                    }



                }
                else
                {
                    arr[0]=0;
                    for(int k=1;k<count1;k++)
                        arr[k]=9;
                    break;
                }
            }
        }
        cout<<"Case #"<<h<<": ";
        for(int i=0;i<count1;i++)
        {
            if(arr[i]!=0)
                cout<<arr[i];
        }
        cout<<endl;
    }
    return 0;
}
