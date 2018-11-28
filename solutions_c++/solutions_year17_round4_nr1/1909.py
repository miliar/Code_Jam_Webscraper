#include <fstream>
#include <cmath>
#include <iostream>
#include <vector>
using namespace std;

int main()
{
  ifstream in("A-small-attempt1.in");
  ofstream out("output.txt");

  int T;
  in>>T;
  for(int t=0; t<T; t++)
  {
	int N, P;
    in>>N>>P;
    vector<int> mod[4];
	int ind[4] = {0, 0, 0, 0};
	
	for(int i=0; i<N; i++)
    {		
      int g; in>>g;
      mod[g%P].push_back(g);  	  
	}
	
	int tot = 0;
	int act = P;
	
	bool end = false;
	while(!end)
	{
	  if(act == P) tot++;		
      int val = -1;
	  if(ind[act%P] < mod[act%P].size())
	  {
		val = mod[act%P][ind[act%P]];
        ind[act%P]++;		
	  } 
	  else
	   for(int i=0; i<4; i++)
		if(ind[i] < mod[i].size())
		{
		  val = mod[i][ind[i]];
          ind[i]++;
          break;		  
		}
		//if(t == 2)cout<<val<<" ""\n";
	  if(val != -1)	
       act = val >= act ? P - ((val - act)%P) : act - val;
	  else
	  {
	    end = true;
	    if(act == P) tot--;
	  }
	} 
	out<<"Case #"<<(t+1)<<": "<<tot<<"\n";
  }	  
  
  in.close();
  out.close();  
  return 0;	
}