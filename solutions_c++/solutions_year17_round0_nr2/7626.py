#include<bits/stdc++.h>
using namespace std;
ifstream fin("B-large.in");
ofstream fout("output.in");
bool areSorted(long long int a)
{
    int count = 0;
    long long int n=a;
    while (n != 0)
    {
        n /= 10;
        count++;
    }
    int arr[count];
    count=0;
    n=a;
    while(n>0){
       arr[count]=n%10;
       n=n/10;
       count++;
    }
    for(int i=0;i<count-1;i++){
        if(arr[i]<arr[i+1]){
            return false;
            break;
        }
    }
return true;}

bool arrSorted(int arr[],int n){
    for(int i=0;i<n-1;i++)
        if(arr[i]>arr[i+1])
            return false;
return true;}


int main(){
int t;

fin>>t;
int z=t;
while(t--){
    long long int a;
    fin>>a;
    long long int n=a;
    if(areSorted(n)){
        fout<<"Case #"<<z-t<<": "<<n<<endl;
        continue;
    }
    else{
        int count=0;
        while (n != 0)
        {
            n /= 10;
            count++;
        }
        int arr[count];
        int arr2[count];
        count=0;
        n=a;
        while(n>0){
           arr[count]=n%10;
           n=n/10;
           count++;
        }
        int l=0;
        for(int i=count-1;i>=0;i--){
            arr2[l++]=arr[i];
        }

        for(;;){
            int b;
            for(int i=0;i<count;i++){
                if(arr2[i]!=0){
                    b=i;
                    break;
                }
            }
            int j=0;
            for(int i=b;i<count;i++)
                arr2[j++]=arr2[i];
            count=j;
            if(arrSorted(arr2,count))
                break;

            for(l=0;l<count-1;l++){
                if(arr2[l]>arr2[l+1]){
                    arr2[l++]--;
                    break;
                }
            }
            for(int i=l;i<count;i++){
                arr2[i]=9;
            }

            //for(int i=0;i<count;i++)
              //  fout<<arr2[i];

            //fout<<" "<<count<<" "<<arrSorted(arr2,count)<<endl;


        }
        fout<<"Case #"<<z-t<<": ";
        for(int i=0;i<count;i++)
          fout<<arr2[i];

        fout<<endl;
    }
}

return 0;}
