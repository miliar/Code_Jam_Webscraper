#include<iostream>
#include<stdio.h>
using namespace std;
int i=0;
int decre(int arr[],int x){
    arr[x]=9;
    if(arr[x-1]==0)
      {x=decre(arr,x-1);}
    else
        arr[x-1]=arr[x-1]-1;
    return x;
}

int main(){

    freopen("input.txt","r",stdin);
    freopen ("output.txt","w",stdout);

    int t=0;cin>>t;int y=1;

    while(t--){
        long long int n=0;cin>>n;
        int arr1[20],arr[20],d=0,count=0,j=0;i=19;

         while(n!=0){
            d=n%10;
            arr1[i--]=d;
            n=n/10;
            count++;
         }

         for(i=count-1;i>=0;i--)
            {arr[i]=arr1[19-j];j++;}
         //for(i=0;i<count;i++)
           // cout<<arr[i];
            //cout<<endl;

            i=count-1;j=0;

            while(i!=0){


                if(arr[i]>=arr[i-1])
                    if(arr[i]==0)
                    {arr[i]=9;i=decre(arr,i-1);
                    }
                    else ;
                else{
                    arr[i]=9;
                    for(int k=i;k<count;k++)
                        arr[k]=9;
                    if(arr[i-1]==0)
                       i= decre(arr,i-1);
                    else
                        arr[i-1]=arr[i-1]-1;

                }


            i--;
            }

            int flag=0;
            for(i=0;i<count;i++)
             {
              if(arr[i]==0);
              else break;
             }

             cout<<"Case #"<<y<<": ";
             for(;i<count;i++)
                cout<<arr[i];
            cout<<endl;


    y++;
    }
    return 0;
}
