#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.txt", "w", stdout);
    std::ios::sync_with_stdio(false);
    cin.tie(NULL);
    int t;
    cin>>t;
    for(int h=1;h<=t;h++)
    {
        long long int no;
        int i,j,arr[19]={0},a[19]={0};
        cin>>no;
        i=1;
        while(no)
        {
           a[i]=no%10;
           i++;
           no/=10;
        }
        i--;
        j=1;
        while(i>=1)
        {
            arr[j]=a[i];
            i--;
            j++;
        }

        j--;
        // final array length is j

        for(i=1;i<=j-1;i++)
        {
            if(arr[i+1]<arr[i])
            {
                bool small =true;
                int l =i;
                while(l>=1)
                {
                    if(arr[l-1]!=arr[l])
                    {
                        small = false;
                        break;
                    }
                    l--;
                }

                if(small==false)
                {
                    arr[l]-=1;
                    l++;
                    while(l<=j)
                    {
                        arr[l]=9;
                        l++;
                    }
                    break;
                }
                else if(small==true)
                {
                    arr[1]-=1;
                    for(int k=2;k<=j;k++)
                    {
                        arr[k]=9;
                    }
                    break;
                }


            }

        }
        int f;
        for(f=1;f<=j;f++)
        {
            if(arr[f]!=0)
                break;
        }
        cout<<"Case #"<<h<<": ";
        for(;f<=j;f++)
                    {

                        cout<<arr[f];
                    }
                    cout<<endl;
    }
    return 0;
}
