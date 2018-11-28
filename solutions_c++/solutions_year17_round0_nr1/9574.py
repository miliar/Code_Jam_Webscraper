#include <bits/stdc++.h>
#define lli long long int
#define ThobdaNeechehaiBC '-'
#define ThobdaUpparkaUpparHiRahegaBc '+'
using namespace std;
char flip(char);
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int ItsnotjustacounterwhichwillbethefinalanswerItssomethingmuchbetterthanthatandiwantsomethingjustlikethisdododododoododododooiwantsomethingjustlikethisdodoododoodoododdodooododod,impos,totalte;
	cin>>totalte;
	int LengthofthedamnPancakeFlipper,ishapathmaykyaboluretrerekomalumhainamekokoipanganahimangtahaibossnahimangtahaibossmatlabnahimagtaichnahihainayarr,jforJOKERtheloopVariableWhichIsNoneotherthanmyoldfriendthatiuseforloopsthatisJ;
	
	for(int testcase=1;testcase<=totalte;testcase++)
	{
	   string THeBigLengthOfTHepancakesInaRow;//    ---+-++-
	   cin>>THeBigLengthOfTHepancakesInaRow>>LengthofthedamnPancakeFlipper;
	   int len=THeBigLengthOfTHepancakesInaRow.length();
	   // 3
	   
	    ItsnotjustacounterwhichwillbethefinalanswerItssomethingmuchbetterthanthatandiwantsomethingjustlikethisdododododoododododooiwantsomethingjustlikethisdodoododoodoododdodooododod=0;impos=0;
	   for(ishapathmaykyaboluretrerekomalumhainamekokoipanganahimangtahaibossnahimangtahaibossmatlabnahimagtaichnahihainayarr=0;ishapathmaykyaboluretrerekomalumhainamekokoipanganahimangtahaibossnahimangtahaibossmatlabnahimagtaichnahihainayarr<len;ishapathmaykyaboluretrerekomalumhainamekokoipanganahimangtahaibossnahimangtahaibossmatlabnahimagtaichnahihainayarr++)
	   {
	    if(THeBigLengthOfTHepancakesInaRow[ishapathmaykyaboluretrerekomalumhainamekokoipanganahimangtahaibossnahimangtahaibossmatlabnahimagtaichnahihainayarr]==ThobdaUpparkaUpparHiRahegaBc)continue;
		//ThobdaNeechehaiBC
		if(ishapathmaykyaboluretrerekomalumhainamekokoipanganahimangtahaibossnahimangtahaibossmatlabnahimagtaichnahihainayarr+LengthofthedamnPancakeFlipper>len){impos=1;break;}
		ItsnotjustacounterwhichwillbethefinalanswerItssomethingmuchbetterthanthatandiwantsomethingjustlikethisdododododoododododooiwantsomethingjustlikethisdodoododoodoododdodooododod++;
		for(jforJOKERtheloopVariableWhichIsNoneotherthanmyoldfriendthatiuseforloopsthatisJ=ishapathmaykyaboluretrerekomalumhainamekokoipanganahimangtahaibossnahimangtahaibossmatlabnahimagtaichnahihainayarr;jforJOKERtheloopVariableWhichIsNoneotherthanmyoldfriendthatiuseforloopsthatisJ<ishapathmaykyaboluretrerekomalumhainamekokoipanganahimangtahaibossnahimangtahaibossmatlabnahimagtaichnahihainayarr+LengthofthedamnPancakeFlipper;jforJOKERtheloopVariableWhichIsNoneotherthanmyoldfriendthatiuseforloopsthatisJ++)
		{
		 THeBigLengthOfTHepancakesInaRow[jforJOKERtheloopVariableWhichIsNoneotherthanmyoldfriendthatiuseforloopsthatisJ]=flip(THeBigLengthOfTHepancakesInaRow[jforJOKERtheloopVariableWhichIsNoneotherthanmyoldfriendthatiuseforloopsthatisJ]);
		}
	   }
	   if(impos==1){cout<<"Case #"<<testcase<<": "<<"IMPOSSIBLE\n";}
	   else{cout<<"Case #"<<testcase<<": "<<ItsnotjustacounterwhichwillbethefinalanswerItssomethingmuchbetterthanthatandiwantsomethingjustlikethisdododododoododododooiwantsomethingjustlikethisdodoododoodoododdodooododod<<endl;}
	}//end of cases
    return 0;
}
char flip(char dgsfhdysgtfysdyufgvfuygvyufgvyugfdygvufduvgfdgvugfvfdgvuyfdgvfdgvfd)
{
    if(dgsfhdysgtfysdyufgvfuygvyufgvyugfdygvufduvgfdgvugfvfdgvuyfdgvfdgvfd==ThobdaUpparkaUpparHiRahegaBc)return ThobdaNeechehaiBC;
    else return ThobdaUpparkaUpparHiRahegaBc;
}