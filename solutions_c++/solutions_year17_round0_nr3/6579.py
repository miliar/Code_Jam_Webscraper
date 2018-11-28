#include <bits/stdc++.h>

using namespace std;

int main()
{
  ifstream fin("input.in");
  ofstream fout("output.txt");
  if(!fin.is_open())cout<<"in not found"<<endl;
  if(!fout.is_open())cout<<"out not found"<<endl;
  int t;
  fin>>t;
  for(int h=1;h<=t;h++){
    int n,k;
    fin>>n>>k;
    int a[n+2];
    fill(a,a+n+2,0);
    a[0]=a[n+1]=1;
    int i=0,j=n+1,l,f,r;
    while(k--){
           int maxdiff=0;
            bool fi=false,la=false;
        for(int I=0;I<n+2;I++){
            if(a[I]==1&&!fi){f=I;fi=true;}
            else if(a[I]==1&&!la){l=I;la=true;}
            if(fi&&la){
                if(l-f>maxdiff){
                    maxdiff=l-f;
                    fi=false;la=false;
                    i=f;j=l;
                    I--;
                }
            }
        }
        r=(i+j)/2;
        a[r]=1;
    }
    int conmin=0,conmax=0;
    for(int k=r+1;k<n+2;k++){
        if(a[k]==0)conmax++;
        else break;
    }
    for(int k=r-1;k>=0;k--){
        if(a[k]==0)conmin++;
        else break;
    }
    fout<<"Case #"<<h<<": "<<max(conmax,conmin)<<" "<<min(conmax,conmin)<<endl;
  }
  fin.close();
  fout.close();
    return 0;
}

