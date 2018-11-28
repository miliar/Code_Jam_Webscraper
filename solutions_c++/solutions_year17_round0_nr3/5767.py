#include <iostream>
#include <string>
#include <vector>
#include <tuple>
#include<list>
#include <algorithm>
using namespace std;
 
typedef tuple<long long int,long long int,long long int> mytuple;
 
bool myf (const mytuple &x, const mytuple &y){
     if( (get<0>(x))>(get<0>(y)))
        return ((get<0>(x))>(get<0>(y)));
     else if((get<0>(x))==(get<0>(y)))
        return ((get<1>(x))<(get<1>(y)));
     return ((get<0>(x))>(get<0>(y)));
 // return get<1>(lhs) < get<1>(rhs);
}
 void fun()
     {
 long long int s,len,i,k=0,e,n,p,p_copy,lhs,rhs;
     lhs=0;
     rhs=0;
      tuple<long long int,long long int,long long int> prev,x,y;
    cin>>n>>p;
  vector<mytuple> data;
    vector<long long int>arr;
    arr.assign(n,0);
    data.push_back(make_tuple(n,0,n-1));
 // data.push_back(make_tuple(9,4,1));
  //  data2.copy(data.begin(),data.end());
  sort(data.begin(),data.end(),myf);
 /* for(vector<mytuple>::iterator iter = data.begin(); iter != data.end(); iter++){
    cout << get<0>(*iter) << "\t" << get<1>(*iter) << "\t" << get<2>(*iter) << endl;
  }*/
     p_copy=p-1;
    i=1;
    while(p_copy--)
        {
    //    cout<<"i is---"<<i<<endl;

        if((get<0>(data[0]))%2==0)
            {
            
            //even//len//start//end
          
           len= get<0>(data[0]);
              s= get<1>(data[0]);
               e= get<2>(data[0]);
            data.erase(data.begin());
            long long int div=s+len/2-1;
            arr[ div]=i;
            //divide in two
            if(len>1)
                {
            get<0>(x)=div-s;
             get<1>(x)=s;
              get<2>(x)=div-1;
            data.push_back(x);
              get<0>(y)=e-div;
             get<1>(y)=div+1;
              get<2>(y)=e;
            data.push_back(y);
            sort(data.begin(),data.end(),myf);
            }
            
      //      cout<<"in even part after sprte\n";
        //     for(vector<mytuple>::iterator iter = data.begin(); iter != data.end(); iter++)
    //cout << get<0>(*iter) << "\t" << get<1>(*iter) << "\t" << get<2>(*iter) << endl;
      //      cout<<"array satus is --\n";
        //    for(k=0;k<arr.size();k++)
          //      cout<<arr[k];
           // cout<<endl;
            //cout<<"**********************\n";
         
             }
        else
            {
          
            //even//len//start//end
           // tuple<long long int,long long int,long long int> prev,x,y;
           len= get<0>(data[0]);
              s= get<1>(data[0]);
               e= get<2>(data[0]);
           data.erase(data.begin());
            long long int div=s+len/2;
            arr[ div]=i;
            //divide in two
            if(len>1)
                {
            get<0>(x)=div-s;
             get<1>(x)=s;
              get<2>(x)=div-1;
            data.push_back(x);
              get<0>(y)=e-div;
             get<1>(y)=div+1;
              get<2>(y)=e;
            data.push_back(y);
            sort(data.begin(),data.end(),myf);
            }
             //cout<<"in odd part after sprte\n";
             //for(vector<mytuple>::iterator iter = data.begin(); iter != data.end(); iter++)
   // cout << get<0>(*iter) << "\t" << get<1>(*iter) << "\t" << get<2>(*iter) << endl;
     //        cout<<"array satus is --\n";
       //     for(k=0;k<arr.size();k++)
         //       cout<<arr[k];
           // cout<<endl;
            //cout<<"**********************\n";
        }
        i++;
    }
    //cout<<"####################################################################\n";
     if((get<0>(data[0]))%2==0)
            {
            
            //even//len//start//end
          
           len= get<0>(data[0]);
              s= get<1>(data[0]);
               e= get<2>(data[0]);
            data.erase(data.begin());
            long long int div=s+len/2-1;
         for(k=div-1;k>=0;k--)
             {
             if(arr[k]==0)
                 lhs++;
             else
                 break;
         }
           for(k=div+1;k<=n-1;k++)
             {
             if(arr[k]==0)
                 rhs++;
             else
                 break;
         }
            arr[ div]=i;
            //divide in two
            if(len>1)
                {
            get<0>(x)=div-s;
             get<1>(x)=s;
              get<2>(x)=div-1;
            data.push_back(x);
              get<0>(y)=e-div;
             get<1>(y)=div+1;
              get<2>(y)=e;
            data.push_back(y);
            sort(data.begin(),data.end(),myf);
            }
            
      //      cout<<"in even part after sprte\n";
        //     for(vector<mytuple>::iterator iter = data.begin(); iter != data.end(); iter++)
    //cout << get<0>(*iter) << "\t" << get<1>(*iter) << "\t" << get<2>(*iter) << endl;
      //      cout<<"array satus is --\n";
        //    for(k=0;k<arr.size();k++)
          //      cout<<arr[k];
            //cout<<endl;
            //cout<<"**********************\n";
         
             }
        else
            {
          
            //even//len//start//end
           // tuple<long long int,long long int,long long int> prev,x,y;
           len= get<0>(data[0]);
              s= get<1>(data[0]);
               e= get<2>(data[0]);
           data.erase(data.begin());
            long long int div=s+len/2;
             for(k=div-1;k>=0;k--)
             {
             if(arr[k]==0)
                 lhs++;
             else
                 break;
         }
           for(k=div+1;k<=n-1;k++)
             {
             if(arr[k]==0)
                 rhs++;
             else
                 break;
         }
            arr[ div]=i;
            //divide in two
            if(len>1)
                {
            get<0>(x)=div-s;
             get<1>(x)=s;
              get<2>(x)=div-1;
            data.push_back(x);
              get<0>(y)=e-div;
             get<1>(y)=div+1;
              get<2>(y)=e;
            data.push_back(y);
            sort(data.begin(),data.end(),myf);
            }
         /*    cout<<"in odd part after sprte\n";
             for(vector<mytuple>::iterator iter = data.begin(); iter != data.end(); iter++)
    cout << get<0>(*iter) << "\t" << get<1>(*iter) << "\t" << get<2>(*iter) << endl;
             cout<<"array satus is --\n";
            for(k=0;k<arr.size();k++)
                cout<<arr[k];
            cout<<endl;
            cout<<"**********************\n";*/
        }
    //cout<<endl;
    cout<<max(lhs,rhs)<<" "<<min(lhs,rhs)<<endl;    
 }
int main(void){
    long long int t,k=1;
    cin>>t;
    while(t--)
        {
       cout << "Case #" << (k++) << ": " ;
        fun();
    }
    
    return 0;
}


