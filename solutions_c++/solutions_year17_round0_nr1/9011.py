#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <string>
#include <cstdio>


using namespace std;  // since cin and cout are both in namespace std, this saves some text
bool last_input_traverser(char *inp,bool *c)
{
	bool p_flag = false;
	bool m_flag = false;
	if(*inp == '+')
		p_flag = true;
	else
		m_flag = true;
	inp++;
	while((*inp)!='\0')
	{
		if(p_flag)
		{
			if(*inp == '-')
			{
				*c = true;
				return false;
			}
		}
		if(m_flag)
		{
			if(*inp == '+')
			{
				*c = true;
				return false;
			}
		}
		inp++;
	}
	return true;
}
int flipper(char *input,int length,int flipper_size,bool* is_impossible)
{
	int count_pass = 0;
	if(length < flipper_size)
	{
		//cout<<"length : "<<length<<" < "<< flipper_size<<endl;
		while(*input!='\0')
		{
			if(*input == '-')
			{
				*is_impossible = true;
				return 0;
			}
			input++;
		}
		return 0;
	}
	else if(length == flipper_size)
	{
		if(last_input_traverser(input,is_impossible))
		{
			if(*input == '+')
				return 0;
			else
				return 1;
		}
		else
		{
			// return impossible;
			return -1;
		}
	}
	else
	{
		while(*input == '+')
		{
			input++;
			count_pass++;
		}
		if(*input == '\0')
			return 0;
		//cout<<"before flipper : "<<input<< " count_pass : "<<count_pass<<endl;
		length-= count_pass;
		if(length < flipper_size)
		{
				*is_impossible = true;
				return -1;
		}
		for(int i=0; i < flipper_size;i++)
		{
			if(*(input+i) == '+')
				*(input+i) = '-';
			else
				*(input+i) = '+';
		}//end for
		/*cout<<"after flipper : "<<input<<endl;
		cout<<"length : "<<length<<endl;*/
		return 1 + flipper(input+1,length-1,flipper_size,is_impossible);
	}
}
	



int main() {
  int t, K, least_step;
  char *hold;
  string S;
  bool h = false;
  bool *is_impossible = &h;
  freopen("A-large.in", "r", stdin);    // redirects standard input
  freopen("A-large.out", "w", stdout);    // redirects standard input
  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
  for (int i = 1; i <= t; ++i) { 
    cin >> S >> K;  // read n and then m.
    hold = &S[0];
	//cout<< "holding : "<<hold<<endl;
	least_step = flipper(hold,S.length(),K,is_impossible);
	//cout<<"is_impossible : "<<*is_impossible<<endl;
	cout<<"CASE #"<<i<<": ";
	if(*is_impossible)
		cout<<"IMPOSSIBLE"<<endl;
	else
		cout<<least_step<<endl;
	*is_impossible = false;
  }
  return 0;
}



