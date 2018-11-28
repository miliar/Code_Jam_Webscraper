#include <iostream>
#include <vector>
#include <algorithm>
#include <sstream>
#include <fstream>
#include <iomanip>
#include <string>

using namespace std;
 
int main()
{
  ifstream jvcin("input.txt");
  ofstream jvcout("output.txt");
  size_t test,t1;
  jvcin >> test;
  for(size_t t1=1;t1<=test;t1++)
  {
  	  unsigned long long n,k;
  	  jvcin >> n;
  	/*bool flag = true;
  	  while(flag)
  	  {
		  stringstream ss;
		  ss << n;
		  string p = ss.str();
		  int m,len = p.length(); 
		  for(m = 0 ; m < len - 1; m++)
		  {
		  	bool kkk = (p[m] == p[m+1]);
		  	cout << kkk << '\n';
		  	if((p[m]>=p[m+1]) || (p[m+1] == '0'))
		  	{
		  		//stringstream convert(p);
		  		//convert >> k;
		  		k = k - 1;
		  		n = (unsigned long long)k;
		  		//printf("%d ",k);
		  	//	cout << n << '\n';
		  		break;
			}
		  }
		  //cout << m;
		  if(m == len - 1) flag = false; 
  	  }*/
  	  bool flag = true;
  	  while(flag)
	  {
	  	k = n;
	  	vector<int> v;
  	    int m,i = 0,len;
		while(k!=0)
	    {
		 v.push_back(k%10);
		 k /= 10;   
		}
		len = v.size();
	    for(m = len - 1 ; m > 0; m--) {
	   	 //cout << v[m] << " " ;
	 	 if((v[m] > v[m-1]) || (v[m-1] == 0))
	     {	
		   n = n - 1;
		   cout << n << "\n";
		   break;
	     }	
	    }
	    if(m == 0) {
			flag = false;
		}
		v.clear();
	  }
	    jvcout << "Case #" << t1 << ": " << n << '\n';
	    //jvcout << fixed;
	    //jvcout << std::setprecision(6) << n  << std::fixed << '\n';
      } 
      jvcin.close();
      jvcout.close();
 // return 0;
}
