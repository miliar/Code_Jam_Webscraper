#include<iostream>
#include<vector>

using namespace std;
bool issortedarray(vector<int> arr, int n)
 {
     for(int i =0; i<n-1; i++)
     {
         if (arr[i]<=arr[i+1])
            {
                continue;
            }
         else
            {
                return false;
            }
     }
     return true;
 }
unsigned long long int Largetidy(unsigned long long int num)
{
    int len, temp, pivot;
    int n[20]={0};
    //cin>>num;
    for(len =0 ; num>0; len++)
    {
        n[len]=num%10;
        num/=10;
    }
    vector <int> rev(len);
    temp=len-1;
    for(int i=0; i<len; i++, temp--)
    {
        rev[i]=n[temp];
    }
    while(true)
    {
        if(issortedarray(rev,len))
        {
            break;
        }
        else
        {
            //find pivot
            for(int i=0; i<len-1; i++)
            {
                if(rev[i]<=rev[i+1])
                    continue;
                else
                {
                    pivot = i;
                    break;
                }
            }
            //pivot operation
            rev[pivot]-=1;
            for(int i = pivot+1; i<len; i++)
            {
                rev[i]=9;
            }
        }
    }
    unsigned long long int k = 0;
    for (int i = 0; i < len; i++)
    {k = 10 * k + rev[i];}
    return k;

}
int main() {
    int t, m;
    unsigned long long int num;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
    cin>>num;
    cout << "Case #" << i << ": " << Largetidy(num)<<endl;
  }
    return 0;
}
