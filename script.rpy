image alex_apartment = "alex_apartment.png"
image parker_co_headquarters = "parker_co_headquarters.png"
image parker_co_lobby = "parker_co_lobby.png"
image campus_cafe = "campus_cafe.png"

# Define variables to track Alex's experience
default alex_experience = 0
default campaign_success = False
default challenge_experience = 0

label start:

    # Initial scene
    scene campus_classroom with fade
    
    # Lisa enters with a move-in effect
    show lisa happy at right with moveinright
    l "Good morning, class! I have some exciting news."
    
     # Alex appears with a dissolve effect
    show alex neutral at center with dissolve
        
    # Alex responds
    a "What is it, Professor Lisa?"
    
    # Lisa continues speaking
    l "Parker & Co. is offering a marketing internship. It's a fantastic opportunity for any aspiring marketer."

    # Tom enters with a move-in effect
    show tom happy at left with moveinleft
    t "Alex, you should totally apply!"
    a "I will! This is the chance I've been waiting for."
    
    # Jenny appears with a move-in effect
    show jenny neutral at left with moveinleft
    
    # Jenny's reaction
    show jenny smirking at left
    j "I am going to apply too. This internship is perfect for me."
    
    # Change scene with a fade effect
    scene alex_apartment with fade
    
    # Alex and Tom appear
    show tom happy at left with moveinleft
    t "Let's prepare for the interview. I'll help you with a mock interview."
       
    show alex thinking at center with dissolve
    a "Thanks, Tom. I appreciate it."
    
    show alex talk at center

     # Mock interview mini-game (simplified) 
    t "Alright let's start."
    t "Why do you want to work at Parker & Co?"
    menu:
        "It's my dream company.":
            a "It's my dream company. The 'Innovate with Us' campaign inspired me. Parker & Co.'s innovative approach and commitment to excellence align with my values. I'm eager to contribute my skills and work to your team."
        "I want to learn from the best.":
            a "I want to learn from the best. Parker & Co.'s cutting-edge strategies and impactful campaigns are renowned. Working here would provide invaluable experience and allow me to contribute my unique skills to your team."
        "I'm not sure.":
            show alex thinking at center
            $ alex_experience -= 1
            a "I'm not really sure. I guess it just seems like a good opportunity."
            
    if alex_experience < 0:
        t "Alex, it sounds like you're struggling with your response. Let's work on improving it together."
        t "You need to convey your passion and how you can contribute to Parker & Co. Think about what excites you about this company and how your skills align with their needs."
        
        menu:
            "Try again: It's my dream company.":
                a "It's my dream company. The 'Innovate with Us' campaign inspired me. Parker & Co.'s innovative approach and commitment to excellence align with my values. I'm eager to contribute my skills and work to your team."
            "Try again: I want to learn from the best.":
                a "I want to learn from the best. Parker & Co.'s cutting-edge strategies and impactful campaigns are renowned. Working here would provide invaluable experience and allow me to contribute my unique skills to your team."
    
    t "Good. Tell me about a successful marketing campaign you've worked on."
    menu:
        "Talk about college project.":
            $ campaign_success = True
            $ alex_experience += 2
            a "In college, I led a marketing campaign for a local bookstore. Our team developed a comprehensive strategy that increased their brand awareness by 20%% within three months. We used targeted social media ads, engaging content, and community events to drive customer engagement."
        "Mention internship experience.":
            $ campaign_success = True
            $ alex_experience += 2
            a "During my internship at XYZ Corp, I managed a social media campaign that boosted engagement by 30%%. We focused on creating interactive content, leveraging influencer partnerships, and utilizing data analytics to optimize our strategies."
        "I haven't worked on any.":
            show alex thinking at center
            $ alex_experience -= 2
            a "I haven't really worked on any marketing campaigns yet."   
    
    if alex_experience < 0:
        t "Alex, it sounds like you need to think more about your experiences. Let's see if we can come up with something."
        t "Think about any project where you applied marketing principles, even if it wasn't a formal campaign. It could be a project in school, a club activity, or even a personal endeavor."
        
        menu:
            "Discuss a school project.":
                a "Actually, I did work on a project in school where we had to market a new club to students. We used posters, social media, and events to increase membership by 25%% in just one semester."
            "Describe a personal project.":
                a "I once helped my friend promote their handmade crafts business. I created an Instagram page and ran a few targeted ads, which increased their sales by 40%% in two months."
    
        t "Wonderful. It sounds like you have a solid foundation. Let's continue preparing."

    show alex happy at center

    # Change scene to Parker & Co. headquarters with a fade effect
    scene parker_co_headquarters with fade
    show alex nervous at center with dissolve

    # Alex's internal dialogue
    a "Here goes nothing."

    # Jenny appears with a move-in effect
    show jenny smirking at left with moveinleft
    
    # Jenny and Alex's dialogue
    j "You think you have a chance? This internship is mine."
    
    show alex angry at center
    a "We'll see about that."

    # Change scene to interview room with a fade effect
    scene interview_room with fade
    show samantha neutral at right with dissolve
    
    # Samantha's dialogue
    s "Welcome, Alex. Let's start the interview."
    
    show alex neutral at center with dissolve
    a "Nice to meet you, Samantha."
    
    show samantha talk at right
    s "How are you feeling?"
    
    show alex blush at center
    a "I'm quite nervous, to be honest. This opportunity means a lot to me."
    
    show samantha huh at right
    s "I understand, and that's completely normal. Just take a deep breath. We'll get through this together."
    
    show alex happy at center
    a "Thank you, I appreciate that."
    
    show samantha talk at right
    s "Alright, let's get started. Are you ready?"
    
    a "Absolutely, let's do this!"
    
    show samantha talk at right
    # Interview scene
    s "Why do you want to work at Parker & Co.?"
    show alex talk at center
    menu:
        "It's my dream company.":
            $ alex_experience += 1
            a "It's my dream company. The 'Innovate with Us' campaign inspired me. Parker & Co.'s innovative approach and commitment to excellence align with my values. I'm eager to contribute my skills and work to your team."
        "I want to learn from the best.":
            $ alex_experience += 1
            a "I want to learn from the best. Parker & Co.'s cutting-edge strategies and impactful campaigns are renowned. Working here would provide invaluable experience and allow me to contribute my unique skills to your team."
        "I don't know.":
            $ alex_experience -= 1
            show alex nervous at center
            a "I don't really know. I guess it just seemed like a good fit."
    
    s "I see. Tell me about a successful marketing campaign you've worked on."
    menu:
        "Talk about college project.":
            $ campaign_success = True
            $ alex_experience += 2
            a "In college, I led a marketing campaign for a local bookstore. Our team developed a comprehensive strategy that increased their brand awareness by 20%% within three months. We used targeted social media ads, engaging content, and community events to drive customer engagement."
        "Mention internship experience.":
            $ campaign_success = True
            $ alex_experience += 2
            a "During my internship at Kane Corp, I managed a social media campaign that boosted engagement by 30%%. We focused on creating interactive content, leveraging influencer partnerships, and utilizing data analytics to optimize our strategies."
        "I don't have any experience.":
            $ alex_experience -= 2
            show alex nervous at center
            a "I don't really have any experience with marketing campaigns."
            
    if campaign_success:
        s "That's excellent. Tell me more about it."
        menu:
            "Talk about college project.":
                $ alex_experience += 1
                a "I worked on a college project where we increased brand awareness by 20%%."
            "Mention internship experience.":
                $ alex_experience += 1
                a "During my internship, I helped launch a social media campaign that boosted engagement by 30%%."
    else:
        s "I see. Let's move on to the next question."
            
    s "Alright thank you. Can you tell me about a time you faced a challenge in a team setting?"
    menu:
        "Group project in college.":
            $ challenge_experience += 1
            $ alex_experience += 1
            a "During a group project in college, one of our team members consistently missed deadlines. I took the initiative to have a one-on-one conversation with them to understand their challenges and offered support. By redistributing tasks and providing clear deadlines, we were able to complete the project on time and with great results."
        "Internship at Kane Corp.":
            $ challenge_experience += 1
            $ alex_experience += 1
            a "At Kane Corp, we faced a tight deadline for a major campaign. One team member was struggling to keep up. I organized a quick brainstorming session to reassign tasks and provide support where needed. This collaborative approach helped us meet the deadline successfully."
        "I haven't faced any challenges.":
            $ alex_experience -= 1
            show alex nervous at center
            a "I haven't really faced any major challenges in a team setting."
        
    if challenge_experience > 0:
        s "Great problem-solving skills. Finally, what motivates you in your work?"
    else:
        s "I see. Finally, what motivates you in your work?"
    menu:
        "Making a difference.":
            $ alex_experience += 1
            a "What motivates me the most is making a difference. I thrive on creating campaigns that not only drive business results but also resonate with people and make a positive impact on their lives."
        "Continuous learning.":
            $ alex_experience += 1
            a "Continuous learning motivates me. The dynamic nature of marketing means there's always something new to learn and explore. I enjoy staying ahead of trends and finding innovative ways to connect with audiences."
        "I'm not sure.":
            $ alex_experience -= 1
            show alex nervous at center
            a "I'm not really sure. I just like doing good work."
    
    # Transition to campaign creation
    show samantha neutral at right
    s "Alright, Alex. Now let's move on to a more practical exercise."

    s "I'd like you to outline a brief marketing campaign for our new product. You can focus on any aspect you think would be most effective."

    # Campaign creation mini-game (simplified)
    menu:
        "Focus on social media.":
            $ alex_experience += 2
            a "I would create a social media campaign targeting young adults with engaging content and interactive posts."
        "Highlight influencer partnerships.":
            $ alex_experience += 2
            a "I would partner with influencers to increase product visibility and credibility."
        "Traditional advertising.":
            $ alex_experience -= 2
            show alex nervous at center
            a "I think we should focus on traditional advertising like print ads and billboards. They have a broad reach and are very effective."
    
    if alex_experience >= 10 and campaign_success and challenge_experience >= 2:
        s "Excellent plan, Alex."
        s "That concludes our interview. Do you have any questions for me?"
        
        a "Yes, I was wondering when I might hear back about the results?"
        
        show samantha neutral at right
        s "We'll review everything and get back to you shortly. You should expect to hear from us within a week."
        
        show alex happy at center
        a "Thank you very much. I appreciate the opportunity."
        
        show samantha happy at right
        s "Thank you, Alex. Have a great day!"
        
        show alex happy at center
        a "You too!"
        
        # Change scene to Parker & Co. lobby with a fade effect
        scene parker_co_lobby with fade
        show samantha neutral at right with dissolve
        show jenny neutral at left with dissolve
        show alex neutral at center with dissolve

        # Announcement of the internship
        s "After careful consideration, we've decided to offer the internship to... Alex Johnson."
        
        show jenny tears at left
        
        show alex blush at center
        a "Thank you so much!"
        
        show samantha happy at right
        j "Congrats, Alex. You earned it."
        
        # Change scene to campus cafe with a fade effect
        scene campus_cafe with fade
        show alex happy at center with dissolve
        show tom happy at left with moveinleft
        show lisa happy at right with moveinright

        # Final congratulations
        l "Well done, Alex!"
        t "I knew you could do it!"
        
        show alex tears at center
        
        a "Thanks, everyone. I couldn't have done it without your support."

        # Alex's final words
        a "I'm ready to start my journey at Parker & Co. and make my mark in the marketing world."
    
    else:
        s "I see. Thank you for your time, Alex."
        s "That concludes our interview. Do you have any questions for me?"
        
        a "Yes, I was wondering when I might hear back about the results?"
        
        show samantha neutral at right
        s "We'll review everything and get back to you shortly. You should expect to hear from us within a week."
        
        show alex neutral at center
        a "Thank you for the opportunity."
        
        show samantha happy at right
        s "Thank you, Alex. Have a great day!"
        
        show alex neutral at center
        a "You too!"

        # Change scene to Parker & Co. lobby with a fade effect
        scene parker_co_lobby with fade
        show samantha neutral at right with dissolve
        show jenny happy at left with dissolve
        show alex neutral at center with dissolve

        # Announcement of the internship
        s "After careful consideration, we've decided to offer the internship to... Jenny Miller."
        
        show jenny happy at left
        
        show alex thinking at center
        a "I appreciate the opportunity. Thank you."
        
        show samantha neutral at right
        s "Thank you, Alex. Best of luck in your future endeavors."

        # Change scene to campus cafe with a fade effect
        scene campus_cafe with fade
        show alex thinking at center with dissolve
        show tom upset at left with moveinleft
        show lisa upset at right with moveinright

        # Consolation
        l "I'm sorry, Alex. You gave it your best shot."
        t "There will be other opportunities. Don't give up."

        show alex tears at center
        
        a "Thanks, everyone. I'll keep pushing forward and seize the next opportunity that comes my way."

    # End of the game
    return