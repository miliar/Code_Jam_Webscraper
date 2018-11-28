#include<iostream>
#include<stdio.h>
#include<cstring>
#include<cstdio>
#include<stdlib.h>
#include<sstream>
#include<list>
#include<math.h>
#include<map>
#include<set>
#include<cstdlib>
#include<cctype>
#include<cmath>
#include<fstream>
#include<vector>
#include<algorithm>
#include <queue>
#include<string>
#include<cstring>
#include <deque>
#include<stack>
using namespace std;


#define ALL(a) a.begin(),a.end()
#define CLR(a) memset(a,0,sizeof(a))
#define PB push_back
#define PI acos(-1.0)
#define READ freopen("input.txt", "r", stdin)
#define WRITE freopen("output.txt", "w", stdout)
long long GCDFast(long long a,long long b){   while(b)b^=a^=b^=a%=b;  return a;   }
#define SET(a) memset(a,-1,sizeof(a))
#define ALL_BITS ((1 << 31) - 1)
#define NEG_BITS(mask) (mask ^= ALL_BITS)
#define TEST_BIT(mask, i) (mask & (1 << i))
#define ON_BIT(mask, i) (mask |= (1 << i))
#define OFF_BIT(mask, i) (mask &= NEG_BITS(1 << i))
#define max3(a,b,c) max(a,max(b,c))
#define min3(a,b,c) min(a,min(b,c))
#define MOD 1000000007
#define MX 100010
#define pii pair<int,int>
#define LL long long
// UP, RIGHT, DOWN, LEFT, UPPER-RIGHT, LOWER-RIGHT, LOWER-LEFT, UPPER-LEFT
int dx[8] = {-1, 0, 1, 0, -1, 1,  1, -1};
int dy[8] = { 0, 1, 0,-1,  1, 1, -1, -1};

long long GCD(long long b, long long a)
{
	if(a == 0)
		return b;
	return GCD(a, b%a);
}
long long getLCM(long long a,long long b){
	long long c=a/GCD(a,b);
	return b*c;
}
map<LL,int>mymap;
map<LL,int>::iterator it;
vector<LL>results;
void createStructure(){
LL twoDig,threeDig,j,num,k,l,x,y;
	{
		for(j=1;j<=9;j++)
		{
			mymap[j]++;
			num= j;
			x = num;
			x*=10;
			for(k=j;k<=9;k++){
				mymap[x+k];//2nd digit
				twoDig=x+k;
				twoDig*=10;
				for(int three=k;three<=9;three++){
					mymap[twoDig+three];//three
					threeDig=twoDig+three;
					threeDig*=10;
					for(int four=three;four<=9;four++){
						mymap[threeDig+four];//four
						LL fourDig=threeDig+four;
						fourDig*=10;
						for(int five=four;five<=9;five++){
							mymap[fourDig+five];//five
							LL fiveDig=fourDig+five;
							fiveDig*=10;
							for(int six=five;six<=9;six++){
								mymap[fiveDig+six];//six
								LL sixDig=fiveDig+six;
								sixDig*=10;
								for(int seven=six;seven<=9;seven++){
									mymap[sixDig+seven];//seven
									LL sevDig=sixDig+seven;
									sevDig*=10;
									for(int eight=seven;eight<=9;eight++){
										mymap[sevDig+eight];//eight
										LL eitDig=sevDig+eight;
										eitDig*=10;
										for(int nine=eight;nine<=9;nine++){
											mymap[eitDig+nine];//nine
											LL nineDig=eitDig+nine;
											nineDig*=10;
											for(int ten=nine;ten<=9;ten++){
												mymap[nineDig+ten];//ten
												LL tenDig=nineDig+ten;
												tenDig*=10;
												for(int eleven=ten;eleven<=9;eleven++){
													mymap[tenDig+eleven];//eleven
													LL eleDig=tenDig+eleven;
													eleDig*=10;
													for(int twlve=eleven;twlve<=9;twlve++){
														mymap[eleDig+twlve];//twelve
														LL twlvDig=eleDig+twlve;
														twlvDig*=10;
														for(int thrten=twlve;thrten<=9;thrten++){
															mymap[twlvDig+thrten];//13
															LL thirtenDig=twlvDig+thrten;
															thirtenDig*=10;
															for(int forten=thrten;forten<=9;forten++){
																mymap[thirtenDig+forten];//14
																LL fortenDig=thirtenDig+forten;
																fortenDig*=10;
																for(int fiften=forten;fiften<=9;fiften++){
																	mymap[fortenDig+fiften];//15
																	LL fiftenDig=fortenDig+fiften;
																	fiftenDig*=10;
																	for(int sixten=fiften;sixten<=9;sixten++){
																		mymap[fiftenDig+sixten];//16
																		LL sixtenDig=fiftenDig+sixten;
																		sixtenDig*=10;
																		for(int seventen=sixten;seventen<=9;seventen++){
																			mymap[sixtenDig+seventen];//17
																			LL seventenDig=sixtenDig+seventen;
																			seventenDig*=10;
																			for(int eitten=seventen;eitten<=9;eitten++){
																				mymap[seventenDig+eitten];//18
																			}
																		}
																	}
																}
															}
														}
													}
												}
											}
										}
									}
								}
							}
						}
					}
				}
			}

		}
	}
}
int main() {
	freopen ("d:/Codejam/B-large.in","r",stdin);
	freopen ("d:/Codejam/output1.txt","w",stdout);
	LL n,i,j,k,temp,m;
	LL x,y,z,sum,test_case=0,length,ans,test,l,w,num;
	string str, str1;
	i=1;
	
	createStructure();
	mymap[1e18]++;
	for(it = mymap.begin(); it!=mymap.end();it++){
		results.push_back(it->first);
	}
	cin>>x;
	i=0;
	while(x--){
		
		cin>>n;
		printf("Case #%lld: ",++test_case);
		std::vector<LL>::iterator lowit;
		lowit = results.begin();
		lowit = std::lower_bound (results.begin(), results.end(), n);
		if(*lowit !=n || n==1e18)
		lowit--;
		cout<<*lowit<<"\n";
		i++;
	}
	
	return 0;
}