#include <stdio.h>
#include <string.h>
#include <vector>
#include <string>
#include <assert.h>
#include <map>

using std::vector;
using std::map;
using std::string;

string s_replace(const string& s,char c,const string& rep)
{
	string ret = "";
	for(size_t j = 0;j < s.size();++j)
	{
		if(s[j] != c) ret.push_back(s[j]);
		else
		{
			ret.push_back(s[j]);
			ret += rep;
			ret += s.substr(j+1);
			break;
		}
	}
	return ret;
}

int main()
{
	//freopen("E:\\dev\\product\\zzprivate_work\\libcpp\\problem\\dessert\\gcj\\2017\\R2_B_\\B-small-attempt0.in","r",stdin);
	static const size_t size = 2000;
	unsigned int nCases = 0;scanf("%d",&nCases);
	for(unsigned int iCases = 1;iCases <= nCases;++iCases)
	{
		unsigned int n = 0,r = 0,o = 0,y = 0,g = 0,b = 0,v = 0;
		scanf("%d%d%d%d%d%d%d",&n,&r,&o,&y,&g,&b,&v);
		bool possible = true;
		if(o > b) possible = false;
		else if(g > r) possible = false;
		else if(v > y) possible = false;
		string ans = "";
		if(possible)
		{
			string s1 = "",s2 = "",s3 = "";
			for(unsigned int i = 0;i < o;++i) s1 += "OB";
			for(unsigned int i = 0;i < g;++i) s2 += "GR";
			for(unsigned int i = 0;i < v;++i) s3 += "VY";
			b -= o;r -= g;y -= v;

			int ry = 0,rb = 0,yr = 0,yb = 0,br = 0,by = 0;
			for(unsigned int i = 0;i <= r;++i)
			{
				ry = i;
				rb = r - ry;
				by = y - ry;
				br = b - by;
				yr = r - br;
				yb = y - yr;
				if(rb < 0 || by < 0 || br < 0 || yr < 0 || yb < 0) continue;
				//printf("#### %d %d %d %d %d %d\n",ry,rb,by,br,yr,yb);
				// ¹¹Ôì
				if(0 != r) ans.push_back('R');
				else if(0 != y) ans.push_back('Y');
				else if(0 != b) ans.push_back('B');

				char prev = ans[0];
				while((ry + rb + yr + yb + by + br) != 0)
				{
					if('R' == prev)
					{
						if(ans[0] == 'Y')
						{
							if(0 != rb) { prev = 'B';--rb; }
							else if(0 != ry) { prev = 'Y';--ry; }
							else assert(0);
						}
						else
						{
							if(0 != ry) { prev = 'Y';--ry; }
							else if(0 != rb) { prev = 'B';--rb; }
							else assert(0);
						}
						ans.push_back(prev);
					}
					else if('Y' == prev)
					{
						if(ans[0] == 'R')
						{
							if(0 != yb) { prev = 'B';--yb; }
							else if(0 != yr) { prev = 'R';--yr; }
							else assert(0);
						}
						else
						{
							if(0 != yr) { prev = 'R';--yr; }
							else if(0 != yb) { prev = 'B';--yb; }
							else assert(0);
						}
						ans.push_back(prev);
					}
					else if('B' == prev)
					{
						if(ans[0] == 'R')
						{
							if(0 != by) { prev = 'Y';-- by; }
							else if(0 != br) { prev = 'R';--br; }
							else assert(0);
						}
						else
						{
							if(0 != br) { prev = 'R';--br; }
							else if(0 != by) { prev = 'Y';-- by; }
							else assert(0);
						}

						ans.push_back(prev);
					}
				}
				ans = ans.substr(0,ans.size()-1);
				ans = s_replace(ans,'B',s1);
				ans = s_replace(ans,'R',s2);
				ans = s_replace(ans,'Y',s3);

				if(0 == ans.size())
				{
					if(s1.size() != 0)
					{
						ans = s1;
						assert(s2.size() == 0 && s3.size() == 0);
					}
					else if(s2.size() != 0)
					{
						ans = s2;
						assert(s1.size() == 0 && s3.size() == 0);
					}
					else if(s3.size() != 0)
					{
						ans = s3;
						assert(s2.size() == 0 && s1.size() == 0);
					}
				}


				break;
			}
		}

		if(0 == ans.size()) possible = false;
		if(!possible) printf("Case #%d: IMPOSSIBLE\n",iCases);
		else
		{
			printf("Case #%d: %s\n",iCases,ans.c_str());
		}
	}
	return 0;
}