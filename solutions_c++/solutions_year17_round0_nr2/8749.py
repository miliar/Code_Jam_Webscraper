#include <iostream>
 #include <sstream>
#include<string>
using namespace std;
 long long int count =0,count1=0;
 string prev ;

bool iscorrect(string str,long long int n)
{
  long long int i,j;
  for(i=0;i<n-1;i++)
  {
    if(str.at(i)>str.at(i+1))
      { return false;}
    
  } return true;
}

bool isgreater(string str2,string str1)
{
  if(str2>=str1)
  {
    return true;
  }
  return false;
}
void findStrictlyIncreasingNum(string str1,long long int start, string out, long long int n,long long int k)
{
    // If number becomes N-digit, prlong long int it
    if (n == 0)
    {
       if(isgreater(out,str1))
        { 
          
          //cout<<"yaha "<<endl;
          if(count1!=0)

          {
            count++;
            cout<<"Case #"<<k<<": "<<prev<<endl;
          }
          return;
      }
        else { 
            count1++;
            prev =out; return;
           }
    }
 
   
    for (long long int i = start; i <= 9; i++)
    {
 
        if(count>=1){return ;}         
        string str;          
        ostringstream temp;  
        temp<<i;
        str=temp.str();
        
        str =   out + str;
 
        findStrictlyIncreasingNum(str1,i + 0, str, n - 1,k);
    }if(count>=1){return ;}  
     
}

 
 int main()
{
  long long int t;
  cin>>t;
  long long int k=0;
  while(t--)
  {
    k++;
      long long int i,j;
      string str;
      cin>>str;
       int n = str.length();
       if(iscorrect(str,n)){cout<<"Case #"<<k<<": "<<str<<endl; continue;}
       else {
        findStrictlyIncreasingNum(str,1, "", n,k);
        if(count==0)
          {
            string xxx = "";
            for(int y =0;y<n-1;y++)
            {
              xxx = xxx + "9";
            } cout<<"Case #"<<k<<": "<<xxx<<endl;
          }
        count =0;count1=0;
      }
    
    }
}