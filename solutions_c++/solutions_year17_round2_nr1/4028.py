#include<bits/stdc++.h>
using namespace std;
#define ll long long int

void merge(ll arr[],ll arr1[], ll l, ll m, ll r)
{


    ll i, j, k;
    ll n1 = m - l + 1;
    ll n2 =  r - m;
    ll L[n1], R[n2];
    ll l1[n1],r1[n2];
    for (i = 0; i < n1; i++)
    {
        l1[i]=arr1[l+i];
        L[i] = arr[l + i];
    }
    for (j = 0; j < n2; j++)
    {
        r1[j]=arr1[m+1+j];

        R[j] = arr[m + 1+ j];
    }
    i = 0;
    j = 0;
    k = l;
    while (i < n1 && j < n2)
    {
        if (L[i] <= R[j])
        {
            arr[k] = L[i];
            arr1[k]=l1[i];
            i++;
        }
        else
        {
            arr[k] = R[j];

            arr1[k]=r1[j];
            j++;
        }
        k++;
    }
    while (i < n1)
    {
        arr[k] = L[i];
        arr1[k]=l1[i];
        i++;
        k++;
    }
    while (j < n2)
    {
        arr[k] = R[j];
        arr1[k]=r1[j];
        j++;
        k++;
    }
}

void mergeSort(ll arr[],ll arr1[], ll l,ll r)
{
    if (l < r)
    {
        ll m = l+(r-l)/2;
        mergeSort(arr,arr1, l, m);
        mergeSort(arr,arr1, m+1, r);

        merge(arr,arr1, l, m, r);
    }
}
int main()
{
     int t;
    cin>>t;
    for(int i=1;i<=t;i++)
    {
       long  long int d,n;
        cin>>d>>n;
      long  long int dist[n],spe[n];
        for(long long int j=0;j<n;j++)
        {
            cin>>dist[j]>>spe[j];
            dist[j]=d-dist[j];
        }
mergeSort(dist,spe, 0, n - 1);
 double tma=0.000000,t=0.000000;
for( long long int j=0;j<n;j++)
{
    t=(dist[j]*1.000000)/(spe[j]*1.000000);
    if(t>=tma) tma=t;
cout<<"T="<<tma<<endl;
}
double speed=(d*1.000000)/tma;
printf("case #%d: %0.6lf\n",i,speed);

    }





    return 0;
}
