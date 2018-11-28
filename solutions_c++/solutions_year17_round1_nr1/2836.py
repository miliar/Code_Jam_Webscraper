#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

#define DEBUG 0

vector<string> grid;
vector<string> answer;
int rows,cols;

class Region
{
	public:
	char initial;
	int min_row,max_row;
	int min_col,max_col;
	Region (int min_r, int max_r, int min_c, int max_c, int i)
	{
		min_row=min_r; max_row=max_r;
		min_col=min_c; max_col=max_c;
		initial=i;
	}
	bool extend_row_up()
	{
		bool can_extend=false;
		if (min_row>0)
		{
			can_extend=true;
			for (int c=min_col; c<=max_col; c++)
			{
				if (answer[min_row-1][c]!='?')
				{
					can_extend=false;
					break;
				}
			}
			if (can_extend)
			{
				min_row--;
				for (int c=min_col; c<=max_col; c++)
				{
					answer[min_row][c]=initial;
				}
			}
		}
		if (DEBUG)
			printf ("Can extend up: %d\n",can_extend);
		return can_extend;
	}
	bool extend_row_down()
	{
		bool can_extend=false;
                if (max_row<rows-1)
                {       
                        can_extend=true;
                        for (int c=min_col; c<=max_col; c++)
                        {       
                                if (answer[max_row+1][c]!='?')
                                {
                                        can_extend=false;
                                        break;
                                }
                        }
                        if (can_extend)
			{
                                max_row++;
				for (int c=min_col; c<=max_col; c++)
				{
					answer[max_row][c]=initial;
				}
               		}
		}
		if (DEBUG)
			printf ("Can extend down: %d\n",can_extend);
		return can_extend;
	}
	bool extend_col_left()
	{
		bool can_extend=false;
                if (min_col>0)
                {       
                        can_extend=true;
                        for (int r=min_row; r<=max_row; r++)
                        {       
                                if (answer[r][min_col-1]!='?')
                                {
                                        can_extend=false;
                                        break;
                                }
                        }
                        if (can_extend)
			{
                                min_col--;
				for (int r=min_row; r<=max_row; r++)
				{
					answer[r][min_col]=initial;
				}
			}
                }
		if (DEBUG)
			printf ("Can extend left: %d\n",can_extend);
		return can_extend;
	}
	bool extend_col_right()
	{
		bool can_extend=false;
                if (max_col<cols-1)
                {
                        can_extend=true;
                        for (int r=min_row; r<=max_row; r++)
                        {
                                if (answer[r][max_col+1]!='?')
                                {
                                        can_extend=false;
                                        break;
                                }
                        }
                        if (can_extend)
			{
                                max_col++;
				for (int r=min_row; r<=max_row; r++)
				{
					answer[r][max_col]=initial;
				}
			}
                }
		if (DEBUG)
			printf ("Can extend right: %d\n",can_extend);
		return can_extend;
	}
	void extend()
	{
		bool extended=true;
		while (extended)
		{
			extended=false;
			extended |= extend_row_up();
			extended |= extend_col_left();
			extended |= extend_row_down();
                        extended |= extend_col_right();
		}
	}
};

vector<Region*> regions;

void min_fill (char initial)
{
	int min_row=rows-1;
	int max_row=0;
	int min_col=cols-1;
	int max_col=0;
	for (int r=0; r<rows; r++)
	{
		for (int c=0; c<cols; c++)
		{
			if (grid[r][c]==initial)
			{
				min_row=min(min_row,r);
				max_row=max(max_row,r);
				min_col=min(min_col,c);
				max_col=max(max_col,c);
			}
		}
	}
	if (DEBUG)
		printf ("Initial: %c, min_row=%d, max_row=%d, min_col=%d, max_col=%d\n", initial,min_row,max_row,min_col,max_col);
	for (int r=min_row; r<=max_row; r++)
	{
		for (int c=min_col; c<=max_col; c++)
		{
			answer[r][c]=initial;
		}
	}
	Region* region=new Region(min_row,max_row,min_col,max_col,initial);
	regions.push_back(region);
}

void print_answer ()
{
	for (int r=0; r<rows; r++)
		cout << answer[r] << endl;
}

int main() {
	int t;
	cin >> t;
	for (int i=0; i<t; i++)
	{
		//vector<string> grid;
		grid.clear();
		answer.clear();
		regions.clear();
		//int rows,cols;
		cin >> rows >> cols;
		for (int r=0; r<rows; r++)
		{
			string row;
			cin >> row;
			grid.push_back(row);
			string blank_row;
			for (int c=0; c<cols; c++)
				blank_row+='?';
			answer.push_back(blank_row);
		}
		for (int r=0; r<rows; r++)
		{
			for (int c=0; c<cols; c++)
			{
				if (isupper(grid[r][c]) && !isupper(answer[r][c]))
				{
					min_fill (grid[r][c]);
				}
			}
		}
		for (int reg=0; reg<regions.size(); reg++)
		{
			if (DEBUG)
				printf ("Extend %d\n", reg);
			regions[reg]->extend();
		}
		printf ("Case #%d:\n",i+1);
		print_answer();
	}
}
