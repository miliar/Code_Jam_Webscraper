#include<iostream>
#include<stdio.h>
#include <cmath>
using namespace std;


int sort(int a[],int n)
{
   int i,j,k,value;
    for(i=1;i<n;i++)//i-->second position to n-1 position
    {
        value=a[i];//storing in temp variable & creating a virtual hole
        for(j=i-1;value<a[j]&&j>=0;j--)
            a[j+1]=a[j];//shifting element to virtual hole
            a[j+1]=value;//filling the hole
    }

    int temp[n];
    for(i=0;i<n;i++)
    temp[n-1-i]=a[i];
    for(i=0;i<n;i++)
    a[i]=temp[i];

   return 0;

}

int next_power(int n){
    int d=0,k=0;
    while(n>=d){
    d=pow(2,k);
    k++;
    }
    return d;
}

int main(){
    freopen("input.txt","r",stdin);
    freopen ("output.txt","w",stdout);

    int t=0;cin>>t;int y=1;

    while(t--){
        int n=0,k=0;cin>>n>>k;

        int z=next_power(n);
        //cout<<z<<endl;

        int arr_max[z],arr_min[z];
        arr_max[0]=n;arr_min[0]=n;

        arr_max[1]=arr_max[0]/2;
        arr_min[1]=(arr_min[0]-1)/2;
        for(int i=1;i<=(z/2);i++){
        arr_max[i*2]=arr_max[i]/2;
        arr_min[i*2]=(arr_max[i]-1)/2;


        arr_max[i*2+1]=(arr_min[i])/2;
        arr_min[i*2+1]=(arr_min[i]-1)/2;

        }


        sort(arr_max,z);
        sort(arr_min,z);

        //for(int i=0;i<z;i++)
        //{cout<<arr_max[i]<<" "<<arr_min[i]<<endl;}

        cout<<"Case #"<<y<<": "<<arr_max[k]<<" "<<arr_min[k];
        cout<<endl;
        y++;
}


return 0;
}
