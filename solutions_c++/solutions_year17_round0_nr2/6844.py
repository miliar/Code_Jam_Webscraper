    #include <iostream>
    #include<string>
    #include<vector>
    using namespace std;
     
    int main() {
    	int t;
    	cin>>t;
      for(int i=1;i<=t;i++)
     	  {string s;
     	  cin>>s;
     	  //cout<<s;
     	  int h;
     	  vector<int> j;
     	  int n=s.size();
     	  for(int b=0;b<n;b++)
     	   { //cout<<s[b]-'0';
     	   	j.push_back(s[b]-'0');
     	  //cout<<j[b];
     	   }
     	   jump:
     	   for(int b=0;b<n-1;b++) 
     	       { if(j[b]>j[b+1])
     	          {for(int q=b+1;q<n;q++)
     	              {j[q]=9;}
     	             if(j[b]!=0)
     	               {j[b]--;}
     	              if(b!=0&&j[b-1]>j[b])
     	                {goto jump;}
     
     	          }
     
     	       }
     	   h=0;
     	   while(j[h]==0&&h<n)
     	    {h++;}
     	    cout<<"Case #"<<i<<": ";
     	    for(int q=h;q<n;q++)
     	      {cout<<j[q];}
     	      cout<<endl;
     	  //  cout<<endl;
     	  }
    	// your code goes here
    	return 0;
    }
