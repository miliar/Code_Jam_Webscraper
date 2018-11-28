#include <iostream>
#include <fstream>
#include <algorithm>
#include <sstream>
#include <cmath>
using namespace std;



long long checknum(string str)
{

	for(int i = 0;i < str.length() - 1; i++)
	{
		if( (str[i] - '0') > (str[i + 1] - '0') )return 0;
	}
	return 1;
}

long long  sparenum(long long  num,long long  leftn , long long  rightn)
{
	stringstream st;
	st << num;
	string str;
	st >> str;

	stringstream st2;
	string astr;
	st2 << rightn;
	st2 >>  astr;
	long long  ck = checknum(str);
	if(checknum(astr) == 1)return rightn;
	if(rightn - 1 == num &&ck== 1)return num;
	else if(rightn - 1 == num && ck == 0)return -1;
	else
	{
		if(ck == 0) //if find num is wrong number
		{
			long long  forrightnum , forleftnum;
			forrightnum = sparenum(ceil((rightn + num )/ 2),num,rightn);
			forleftnum = sparenum(ceil((leftn + num )/ 2),leftn,num);
			long long  maxnum = max(forrightnum,forleftnum);
			return maxnum; 
		}
		else //correct num
		{
			long long  nextnum = sparenum(ceil((rightn + num )/ 2),num,rightn);//go to right side to find the num
			
			if(nextnum == -1)return num;//not found
			else
			{
				if(num < nextnum) return nextnum;
				else return num;
			}//appear and num is correct
		}
	}

}

string misa(string str,int now)
{
	if((str[now] - '0') > 0)
	{
		str[now] = ((str[now] - '0') - 1) + '0';
		/* code */
	}
	else
	{
		str[now] = '9';
		str = misa(str,now - 1);
	}
	return str;
}
string spae(string str)
{
	int now  = str.length() - 1;
	if(now == 0)return str;
	while(now >= 0)
	{
		if(checknum(str) == 1)return str;
		else 
		{
			str[now] = '9';
			if(str[now - 1] > '0')str[now - 1] = ((str[now - 1] - '0') - 1) + '0';
			else
			{
				str = misa(str,now - 1);
			}
			now--;
			
		}
	}
}

int main()
{
	fstream fin;
	fin.open("B-large.in.txt");
	ofstream fout("b.out"); 

	long long  casenum;

	fin >> casenum;
	int counter = 1;
	while(casenum--)
	{

		long long  startnum  = 1, endnum;
		string ednum;
		fin >>  ednum;
		//long long  max = sparenum(ceil((startnum + endnum)/2),startnum,endnum);
		string ansnum = spae(ednum);
		stringstream anst;
		anst << ansnum;
		long long  ansn;
		anst >> ansn;
		fout << "Case #"<< counter++ <<": "<< ansn << endl;
	}


    fout.close(); 

    fin.close();
    return 0;
}