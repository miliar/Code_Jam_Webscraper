#include<fstream>
#include<iostream>
#include<algorithm>
#include<string>

using namespace std;


string solve(string &s)
{  
   if(s.size()==1) return s;
   string res;
    char last,cur;
        int flag,i,j;
   if(s[s.size()-1]=='0') {res.push_back('9'); flag=-1;}
   else { res.push_back(s[s.size()-1]); flag=0;}
  // cout<<res<<"--"<<endl;
   
   for(i=s.size()-2;i>=0;i--)
   {   

        last=res.back();
        cur=s[i]+flag; //  cout<<cur<<" "<<last<<endl;
        if(cur<'0') { cur='9'; flag=-1;}
        else flag=0;
       
        if(cur<=last) res.push_back(cur);
        else { // cout<<"888\n";
                 
                for(j=0;j<res.size();j++) res[j]='9';
                
                //res.erase(res.end()-1); res.push_back('9');
                if(cur=='0') { cur='9'; flag=-1;}
                else { cur-=1; flag=0;}
               
                res.push_back(cur);  
             }
   // cout<<res<<" *\n";

   }

   if(res.back()=='0') res.erase(res.end()-1);
   reverse(res.begin(),res.end());
   return res;
   
}


int main()
{ 
 int n,i,j;
  string num,res;
  ofstream output;
  output.open("outputBlarge.txt");
  
  ifstream input;
  input.open("B-large.in");
  input>>n;
  cout<<n<<endl;
 
  for(j=1;j<=n;j++)
  { //input>>s; //cout<<s<<endl;
    input>>num;
         
    res=solve(num);
    output<<"Case #"<<j<<": "<<res<<endl; 
   // cout<<j<<endl;

  }
  
 input.close();
 output.close();
string s="928";
cout<<solve(s)<<endl;
   return 0;
}
