#ifdef JUDGE
#include<fstream>
#include<vector>
using namespace std;
ifstream cin("input.txt");
ofstream cout("output.txt");
#else
#include<iostream>
#include<vector>
using namespace std;
#endif // JUDGE

int main()
{
    int test;
    cin>>test;
    for(int i=1;i<=test;i++)
    {
        unsigned long long int n;
        cin>>n;
        vector<int> arr;
        while(n)
        {
            arr.push_back(n%10);
            n = n/10;
        }
        int m = arr.size();
        for(int j=0;j<m-1;j++)
        {
            if(arr[j] >= arr[j+1])
            {

            }
            else
            {
                for(int k=0;k<=j;k++)
                {
                    arr[k] = 9;
                }
                arr[j+1] = arr[j+1]-1;
            }
        }
        m=m-1;
        while(arr[m] == 0)
        {
            m--;
        }
        cout<<"Case #"<<i<<": ";
        for(int k=m;k>=0;k--)
        {
            cout<<arr[k];
        }
        cout<<endl;
    }
    return 0;
}
