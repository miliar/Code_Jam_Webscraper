#include <iostream>
#include <string>
#include <sstream>
#include <map>
#include <utility>
#include <vector>
#include <set>
#include <random>
#include <algorithm>
#include <iterator>

struct cakeCoordinate
{
   int x;
   int y;
};

bool expand(char cake[25][25], int rows, int cols, char child, int directionX, int directionY)
{
   std::vector<struct cakeCoordinate> expPts;

   for(int x = 0; x < cols; x++)
   {
      for(int y = 0; y < rows; y++)
      {
         if (cake[x][y] == child)
         {
            int expandX = x + directionX;
            int expandY = y + directionY;

            struct cakeCoordinate expansionPoint;
            expansionPoint.x = expandX;
            expansionPoint.y = expandY;

            expPts.push_back(expansionPoint);
         }
      }
   }

   for(auto singlePoint = expPts.begin(); singlePoint != expPts.end(); singlePoint++)
   {
      cake[singlePoint->x][singlePoint->y] = child;
   }
}

std::string cakeToString(char cake[25][25], int rows, int cols)
{
   std::string retVal;
   for(int y = 0; y < rows; y++)
   {
      for(int x = 0; x < cols; x++)
      {

         retVal += cake[x][y];
      }

      retVal += '\n';
   }

   return retVal;
}


bool canChildExpand(char cake[25][25], int rows, int cols, char child, int directionX, int directionY)
{
   //std::cerr << "canChildExpand(" << child << ", x=" << directionX << ", y=" << directionY << " ... ";

   for(int x = 0; x < cols; x++)
   {
      for(int y = 0; y < rows; y++)
      {
         if (cake[x][y] == child)
         {
            int expandX = x + directionX;
            int expandY = y + directionY;

            // Can this child be expanded ?
            if ( (expandX < 0) || (expandX >= cols))
            {
               // Expand out of x range
               //std::cerr << "Nope" << std::endl;
               return false;
            }

            if ( (expandY < 0) || (expandY >= rows))
            {
               // Expand out of y range
               //std::cerr << "Nope" << std::endl;
               return false;
            }

            if ( (cake[expandX][expandY] != '?') && (cake[expandX][expandY] != child) )
            {
               // Space already taken by some other dumb kids initials
               //std::cerr << "Nope" << std::endl;
               return false;
            }
         }
      }
   }

   //std::cerr << "YES" << std::endl;
   return true;
}

bool isDecorated(char cake[25][25], int rows, int cols)
{
   for(int x = 0; x < cols; x++)
   {
      for(int y = 0; y < rows; y++)
      {
         if (cake[x][y] == '?')
            return false;
      }
   }

   return true;
}

void rotateDirections(std::vector<struct cakeCoordinate>& points)
{
   if (points.size() <= 1)
      return;

   struct cakeCoordinate firstCoord = points.front();

   points.erase(points.begin());
   points.push_back(firstCoord);
}

void rotateChildren(std::vector<char>& children)
{
   if (children.size() <= 1)
      return;

   char firstChild = children.front();

   children.erase(children.begin());
   children.push_back(firstChild);
}

std::string childrenToString(std::vector<char> children)
{
   std::string retVal;
   for(auto childIter = children.begin(); childIter != children.end(); childIter++)
   {
      retVal += *childIter;
   }

   return retVal;
}

void copyCake(char dest[25][25], char src[25][25], int rows, int cols)
{
   for(int x = 0; x < cols; x++)
   {
      for(int y = 0; y < rows; y++)
      {
         dest[x][y] = src[x][y];
      }
   }
}

std::string solveCase()
{
   int rows, cols;
   std::cin >> rows;
   std::cin >> cols;

   char cake[25][25];
   char cakeCopy[25][25];

   std::vector<char> children;

   for(int curRow = 0; curRow < rows; curRow++)
   {
      for(int curCol = 0; curCol < cols; curCol++)
      {
         char nextInitial;
         std::cin >> nextInitial;
         cake[curCol][curRow] = nextInitial;

         if (nextInitial != '?')
         {
            children.push_back(nextInitial);
         }
      }
   }

   std::cerr << "Current Cake:" << std::endl << cakeToString(cake, rows, cols) << std::endl;



   std::cerr << "Children: " << childrenToString(children) << std::endl;

   // Going to shuffle the order of the children over and over until I get a working solution
   std::random_device rd;
   std::mt19937 g(rd());

   std::vector<struct cakeCoordinate> expandDirs;
   expandDirs.push_back({1,0});
   expandDirs.push_back({0,1});
   expandDirs.push_back({-1,0});
   expandDirs.push_back({0,-1});


   bool solved = false;
   while(!solved)
   {
      std::shuffle(children.begin(), children.end(), g);

      std::cerr << "Children: " << childrenToString(children) << std::endl;

      bool didAnyExpand = true;
      copyCake(cakeCopy, cake, rows, cols);
      while(didAnyExpand)
      {
         didAnyExpand = false;
         int numChildren = children.size();
         for(int expandAttempts = 0; expandAttempts < numChildren * expandDirs.size(); expandAttempts++)
         {

            if (isDecorated(cakeCopy, rows, cols))
            {
               solved = true;
               break;
            }

            rotateChildren(children);

            if ( (expandAttempts % numChildren) == 0)
            {
               rotateDirections(expandDirs);
            }

            if (canChildExpand(cakeCopy, rows, cols, children.front(), expandDirs.front().x, expandDirs.front().y))
            {
               expand(cakeCopy, rows, cols, children.front(), expandDirs.front().x, expandDirs.front().y);
               std::cerr << "Cake after expand!" << std::endl << cakeToString(cakeCopy, rows, cols) << std::endl;
               didAnyExpand = true;
            }
         }
      }

      if (!solved && !didAnyExpand)
      {
         std::cerr << "What a giant cluster fuck" << std::endl;
         return "FAILED";
      }



   }

   return cakeToString(cakeCopy , rows, cols);

}

int main(int, char**)
{
   int numCases = 0;
   std::cin >> numCases;

   for(int i = 0; i < numCases; i++)
   {
      std::cout << "Case #" << i+1 << ": " << std::endl << solveCase();
   }

   return 0;
}
