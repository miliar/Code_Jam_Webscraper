#include <bits/stdc++.h>
using namespace std;

int main()
{
    ofstream output("output large.o");
    ifstream input("B-large.in");
    int t;
    input >> t;
    for(int test=1;test<=t;test++)
    {
        string str;
        input >> str;
        int n=str.size();
        int arr[n],i;
        for(i=0;i<n;i++)
            arr[i]=str[i]-'0';
        while(true)
        {
            for(i=0;i<n-1;i++)
            {
                if(arr[i]>arr[i+1])
                {
                    arr[i]--;
                    for(int j=i+1;j<n;j++)
                        arr[j]=9;
                    break;
                }
            }
            if(i==n-1)
                break;
        }
        int start=0;
        if(arr[0]==0)
            start=1;
        output << "Case #" << test << ": ";
        for(i=start;i<n;i++)
            output << arr[i];
        output << endl;
    }
}
