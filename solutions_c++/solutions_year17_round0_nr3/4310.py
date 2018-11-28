#include<bits/stdc++.h>

using namespace std;
long long max(long long x,long long y){
return x>y?x:y;
}
long long min(long long x,long long y){
return x<y?x:y;
}
long long bathStall(long long arr,long long n){

  if(arr==n)
    return 0;

  if(n==1){
    return arr/2;
  }


  return max(bathStall(arr/2-1,n-1),bathStall(arr-arr/2,n-1));
}

void insert(std::vector<long long> &vec, long long new_val) {
    if (vec.empty()) {
        vec.push_back(new_val);
        return;
    }

    vec.resize(vec.size()+1);
    std::vector<long long>::reverse_iterator pos = vec.rbegin();

    for ( ; *(pos+1) > new_val && (pos+1) != vec.rend(); ++pos)
        *pos = *(pos+1);
    *pos = new_val;
}

int main(){

freopen("C-small-2-attempt1.in","r",stdin);

freopen("C-small-2-attempt1.out","w",stdout);
int t;
cin>>t;
long long a[2*t];
for(int i=0;i<2*t;i++){
    cin>>a[i];
}

for(int i=0;i<2*t;i+=2){
       long long arr=a[i];
       long long n=a[i+1];
       long long left=0;
       long long right=0;
       long long resultleft,resultright;
       vector<long long > vec;
       make_heap(vec.begin(),vec.end());
//       long long result=bathStall(arr,n);
        if(n==arr){
            left=0;right=0;
        }
        else{
           while (n>=1){

             if(arr%2==0){
            left=arr/2-1;
            right=arr/2;
            if( right==0)
            {
               left=0;
            }
          //  resultleft=arr/2-1;
          //  resultright=arr/2;
             }else{
            left=arr -((arr+1)/2);
            right=arr -((arr+1)/2);
          //  resultleft=(arr+1)/2;
          //  resultright=(arr+1)/2;
             }

            if( left < right){
            //insert(vec,left);
            vec.push_back(left);
            push_heap(vec.begin(),vec.end());

            if(vec.front()>max(left,right)){
                arr=vec.front();
             pop_heap(vec.begin(),vec.end());
                 vec.pop_back();
                 vec.push_back(right);
            push_heap(vec.begin(),vec.end());
            }
            else
                arr=right;
            }
            else{
            vec.push_back(right);
            push_heap(vec.begin(),vec.end());
            if(vec.front()>max(left,right)){
                arr=vec.front();
            pop_heap(vec.begin(),vec.end());
                vec.pop_back();
                vec.push_back(left);
            push_heap(vec.begin(),vec.end());
            }
             else
                arr=left;
            }


            n--;

           }

        }



    cout<<"Case "<<"#"<<i/2+1<<": "<<max(left,right)<<" "<<min(left,right)<<endl;




}


}



