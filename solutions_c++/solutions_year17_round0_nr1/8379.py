#include<iostream>
#include<algorithm>
using namespace std;
typedef long long LL;
LL K;
string happyAll = "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++";
bool solved = false;
LL minimum;
string invert(string pancakes, LL pos)
{
	for(LL p = pos; p < pos+K; p++)
		if(pancakes[p]=='+')
			pancakes[p]='-';
		else
			pancakes[p]='+';
	return pancakes;
}
void flip(string pancakes, LL pos, LL flipCount)
{
	if(pancakes==happyAll.substr(0,pancakes.length()) ) //solved!
	{
		if(flipCount<=minimum)
		{
			solved = true;
			minimum = flipCount;
		}
	}
	else if(flipCount==minimum) //no real improvement can be made
		return;
	else if(pos+K > pancakes.length()) //reached the end without a solved state
		return;
	else if(pancakes.substr(pos,K)==happyAll.substr(0,K)) //no need to flip	
		flip(pancakes,pos+1,flipCount);
	else if(pancakes[pos]=='-') //first character is a - so I can't pass it up
		flip(invert(pancakes,pos), pos+1, flipCount+1);
	else
	{
		flip(pancakes, pos+1, flipCount);
		flip(invert(pancakes,pos), pos+1, flipCount+1);
	}
}
int main()
{
	LL T;
	string pancakes;
	cin >> T;
	for(LL t = 1; t<= T; t++)
	{
		solved = false;
		cin >> pancakes >> K;
		
		minimum = pancakes.length()-K+1;
		
		flip(pancakes, 0,0);
		if(solved)
			cout<<"Case #"<<t<<": "<<minimum<<endl;
		else
			cout<<"Case #"<<t<<": IMPOSSIBLE"<<endl;
	}
	
	return 0;
}