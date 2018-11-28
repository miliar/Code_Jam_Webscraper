#include <bits/stdc++.h>
using namespace std;


string i2s(int a)
{
	stringstream ss;
	ss << a;
	return ss.str();
}

int flip_size,len_total;
map<string, int> M;

string vec2str(vector<bool> v)
{
	string str="";
	for(int i=0;i<int(v.size());i++)
	{
		if(v[i])
		{
			str+="+";
		}
		else
		{
			str+="-";
		}
	}
	return str;
}

int find_min_flips(vector<bool> v)
{
	// cerr<<"start"<<endl;
	string min_str=vec2str(v);
	if(M.find(min_str) != M.end()) 
	{ 
      return M[min_str]; 
 	} 
	bool zero_ret=true;
	int start_false;
	for(int i=0;i<len_total;i++)
	{
		if(!v[i])
		{
			start_false=i;
			zero_ret=false;
			break;
		}
	}
	if(zero_ret)
	{
		M[min_str]=0;
		return 0;
	}
	vector<int> min_trys;
	for(int i=0;i<=(len_total-flip_size);i++)
	{
		bool should_do=false;
		for(int j=i;j<(i+flip_size);j++)
		{
			if(!v[j])
			{
				should_do=true;
			}
			break;
		}
		if(should_do)
		{
			vector<bool> temp;
			temp=v;
			for(int j=i;j<(i+flip_size);j++)
			{
				temp[j]=(!temp[j]);
			}
			min_trys.push_back(1+find_min_flips(temp));
		}
	}

	int min=INT_MAX;
	for(int i=0;i<int(min_trys.size());i++)
	{
		if(min_trys[i]<min)
		{
			min=min_trys[i];
		}
	}
	M[min_str]=min;

	cerr<<"min is "<<min<<" min_str was:"<<min_str<<endl;
	return min;
}



int main(int argc, char const *argv[])
{
	ifstream infile;
	infile.open(argv[1]);

	int test_case;
	infile>>test_case;
	for(int abc=0;abc<test_case;abc++)
	{
		// cout<<"Case #"<<(abc+1)<<": "<<i<<endl;
		M.clear();
		string str;
		infile>>str>>flip_size;
		len_total=int(str.length());
		vector<bool> myvec(len_total,false);
		for(int i=0;i<len_total;i++)
		{
			if(str.at(i)=='+')
			{
				myvec[i]=true;
			}
		}
		bool IMPOSSIBLE=false;
		bool impos=myvec[len_total-flip_size];
		for(int i=(len_total-flip_size);i<(flip_size-1);i++)
		{
			if(myvec[i]!=impos)
			{
				cout<<"Case #"<<(abc+1)<<": "<<"IMPOSSIBLE"<<endl;
				IMPOSSIBLE=true;
				break;
			}
		}
		if(!IMPOSSIBLE)
		{
			// cout<<"its not IMPOSSIBLE says "<<abc<<endl;
			int pos_ans=find_min_flips(myvec);
			if(pos_ans>100000 || pos_ans<(-100000))
			{				
				cout<<"Case #"<<(abc+1)<<": "<<"IMPOSSIBLE"<<endl;
			}
			else
			{
				cout<<"Case #"<<(abc+1)<<": "<<pos_ans<<endl;	
			}
		}

	}

	return 0;
}

